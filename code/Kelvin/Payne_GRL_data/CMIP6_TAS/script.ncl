; Temperature anomaly w.r.t the mean temperature of the period 1995-2014

begin
mpath = "../../../../data/raw_data/CMIP6_TAS/global_tas_mon_"

expt = (/"CNRM-CM6-1_ssp585","CNRM-CM6-1_ssp126","UKESM1-0-LL_ssp585","CESM2_ssp585", \
        "CNRM-ESM2-1_ssp585","CNRM-CM6-1_ssp585","CNRM-CM6-1_ssp126","UKESM1-0-LL_ssp585", \
        "CESM2_ssp585","CNRM-ESM2-1_ssp585"/)

n_expt = dimsizes(expt)

styr = (/2016,2051/)
edyr = (/2050,2100/)

do i = 0, n_expt-1
        flist := systemfunc("ls "+mpath+expt(i)+"*_ave.dat")
        data := asciiread(flist,-1,"string")
        header := str_match(data,"#")
        n_header = dimsizes(header)
        last_head := header(n_header-1)
        head_ind = ind(data.eq.last_head)
        data_cur := str_sub_str(str_squeeze(data(head_ind+1::))," ",",")
        year := tofloat(str_get_field(data_cur,1,","))
        n_year = dimsizes(year)
        yr_tas := new(n_year,"float")
        do j = 0, n_year-1
                tmp = 0.
                do k = 2, 13
                        field := tofloat(str_get_field(data_cur,k,","))
                        tmp = tmp + field(j)
                end do
                yr_tas(j) = tmp / 12.
        end do

        ind_base_st = ind(year.eq.1995)
        ind_base_ed = ind(year.eq.2014)

        base_line_tas = avg(yr_tas(ind_base_st:ind_base_ed))

        do j = 0, 1
                ind_st = ind(year.eq.styr(j))
                ind_ed = ind(year.eq.edyr(j))
                mean_yr_tas = avg(yr_tas(ind_st:ind_ed))
                mean_yr_tas = mean_yr_tas - base_line_tas
                print(expt(i)+","+styr(j)+","+edyr(j)+","+mean_yr_tas)
        end do



end do
end
