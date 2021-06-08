begin
	path = "../../../../data/raw_data/Landice-Edwards21/proj_MAIN_TIMESERIES"
        scen = (/"119","126","245","370","585","NDC"/)
        n_scen = dimsizes(scen)

; Possible Source
        ;source = (/"GrIS","AIS","Glaciers"/)
        ;n_source = dimsizes(source)

        source = "Glaciers"
        n_sample = 500

        minyr = (/2016,2051/)
        maxyr = (/2050,2100/)
        print("ice_source,region,scenario,minyr,maxyr,median(rateSLE),median(GSAT)")

do k = 0, n_scen-1
                        data_o := asciiread(path+"/projections_FAIR_SSP"+scen(k)+".csv",-1,"string")
                        data := data_o(1::)
        ; ice_source,region,year,sample,GSAT,melt,collapse,SLE
                        ice_source := str_get_field(data,1,",")
                        region := str_get_field(data,2,",")
                        year := toint(str_get_field(data,3,","))
                        sample := toint(str_get_field(data,4,","))
                        gsat := tofloat(str_get_field(data,5,","))
                        sle := tofloat(str_get_field(data,8,","))
                        do j = 0, 1
                                tind := ind(ice_source.eq.source .and. \
                                        year.le. maxyr(j) .and. \
                                        year.ge. minyr(j))
                                tmp_year := year(tind)
                                n_year = maxyr(j) - minyr(j) + 1
                                tmp_sample := sample(tind)
                                tmp_gsat := gsat(tind)
                                tmp_sle := sle(tind)
                        ; Temp output
                                rate_sle := new(n_sample,"float")
                                mean_gsat := new(n_sample,"float")
                                do ii = 1, 500
                                        tmp_gsat_avg := new(n_year,"float")
                                        tmp_sle_sum := new(n_year,"float")
                                        do jj = 0, n_year-1     ; Merge all piece together
                                                tyear = minyr(j) + jj
                                                tind := ind(tmp_sample.eq.ii .and. tmp_year.eq.tyear)  
                                                tmp_sle_sum(jj) = sum(tmp_sle(tind))
                                                tmp_gsat_avg(jj) = avg(tmp_gsat(tind))
                                        end do
                                        rate_sle(ii-1) = avg(tmp_sle(tind))/tofloat(n_year)
                                        mean_gsat(ii-1) = avg(tmp_gsat(tind))
                                end do
                                print(source+",SUM,"+scen(k)+","+ \
                                        minyr(j)+","+maxyr(j)+","+dim_median(rate_sle*10)+ \
                                        ","+dim_median(mean_gsat))

                        end do
                end do
end



