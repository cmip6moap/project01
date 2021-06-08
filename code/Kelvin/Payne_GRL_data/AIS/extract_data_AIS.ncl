; Extract data of AIS
;
; We get the list of files first then process 1 file at a time

begin
	mpath = "~/cmip6_data_hackathon_bristol2021/GRL_paper_data/AIS/Ice"

; List of files
        flist = systemfunc("csh -c 'cd "+mpath+"; ls *.nc'")
        n_file = dimsizes(flist)

        minyr = (/2016,2051/)
        maxyr = (/2050,2100/)
        print("Model_Expt,Minyr,Maxyr,SLErate(mm/yr) R1,SLErate(mm/yr) R2,SLErate(mm/yr) R3")
        do i = 0, n_file-1
                dum := str_split(flist(i),".")
                tdum := str_split(dum(0),"_")
		tdum := tdum(6::)
                n_sec = dimsizes(tdum)
                model_expt_name := tdum(0)      ; This is the model and expt name
                do j = 1, n_sec-1
                        model_expt_name = model_expt_name + "_"+tdum(j)
                end do
                data := addfile(mpath+"/"+flist(i),"r")
                sle1 := (data->limnsw_region_1)/361.
                sle2 := (data->limnsw_region_2)/361.
                sle3 := (data->limnsw_region_3)/361.

                time := data->time
                do j = 0, 1
                        n_year := maxyr(j) - minyr(j) + 1.0
                        ind_mint := ind(time.eq.minyr(j))
                        ind_maxt := ind(time.eq.maxyr(j))
                        sle_sel1 := avg(sle1(ind_mint:ind_maxt)) / n_year
                        sle_sel2 := avg(sle2(ind_mint:ind_maxt)) / n_year
                        sle_sel3 := avg(sle3(ind_mint:ind_maxt)) / n_year
                        print(model_expt_name+","+minyr(j)+","+maxyr(j)+","+sle_sel1+","+sle_sel2+","+sle_sel3)
                end do
        end do


end

