; Extract data of GrIS
;
; We get the list of files first then process 1 file at a time


begin
	mpath = "~/cmip6_data_hackathon_bristol2021/GRL_paper_data/GrIS/Ice"
; List of files
        flist = systemfunc("csh -c 'cd "+mpath+"; ls *.nc'")
        n_file = dimsizes(flist)

        minyr = (/2016,2051/)
        maxyr = (/2050,2100/)
        print("Model_Expt,Minyr,Maxyr,SLErate(mm/yr)")
        do i = 0, n_file-1
                dum := str_split(flist(i),".")
                tdum := str_split(dum(0),"_")
        ; (0) scalars
        ; (1) mm
        ; (2) cr
        ; (3) GIS
                tdum := tdum(4::)
                n_sec = dimsizes(tdum)
                model_expt_name := tdum(0)      ; This is the model and expt name
                do j = 1, n_sec-1
                        model_expt_name = model_expt_name + "_"+tdum(j)
                end do

                data := addfile(mpath+"/"+flist(i),"r")
                sle := data->sle
                if(tdum(0).eq."UAF" .or. tdum(0).eq."UCIJPL")then
                        data := addfile(mpath+"/scalars_mm_cr_GIS_NCAR_CISM_expb05.nc","r")
                end if
                time := floor(cd_calendar(data->time,1)/100)
                do j = 0, 1
                        n_year := maxyr(j) - minyr(j) + 1.0
                        ind_mint := ind(time.eq.minyr(j))
                        ind_maxt := ind(time.eq.maxyr(j))
                        sle_sel := (avg(sle(ind_mint:ind_maxt)) / n_year) * 1000.
                        print(model_expt_name+","+minyr(j)+","+maxyr(j)+","+sle_sel)
                end do
        end do


end
