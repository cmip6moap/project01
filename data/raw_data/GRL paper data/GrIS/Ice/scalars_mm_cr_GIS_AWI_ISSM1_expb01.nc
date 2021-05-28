CDF   V   
      time             nco_openmp_thread_number            Description       PISMIP6-Greenland recalculated scalar output. Heiko Goelzer 2019, h.goelzer@uu.nl   history      �Wed May 13 11:55:59 2020: ncks -A -v oarea,rhof,rhoi,rhow,dx,dy /home/hgoelzer/Projects/ISMIP6/Archive_sc/Data/SC_GIC1_OBS0//AWI/ISSM1/expb01_05/scalars_mm_GIS_AWI_ISSM1_expb01.nc anc_cr_tmp.nc
Wed May 13 11:55:59 2020: ncap2 -O -s *var_tmp=smb(0); smb=float(smb-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 11:55:59 2020: ncap2 -O -s *var_tmp=sle(0); sle=float(sle-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 11:55:59 2020: ncap2 -O -s *var_tmp=limgr(0); limgr=float(limgr-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 11:55:59 2020: ncap2 -O -s *var_tmp=limfl(0); limfl=float(limfl-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 11:55:59 2020: ncap2 -O -s *var_tmp=limaf(0); limaf=float(limaf-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 11:55:58 2020: ncap2 -O -s *var_tmp=lim(0); lim=float(lim-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 11:55:58 2020: ncap2 -O -s *var_tmp=ivolgr(0); ivolgr=float(ivolgr-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 11:55:58 2020: ncap2 -O -s *var_tmp=ivolfl(0); ivolfl=float(ivolfl-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 11:55:58 2020: ncap2 -O -s *var_tmp=ivol(0); ivol=float(ivol-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 11:55:58 2020: ncap2 -O -s *var_tmp=ivaf(0); ivaf=float(ivaf-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 11:55:58 2020: ncap2 -O -s *var_tmp=iareagr(0); iareagr=float(iareagr-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 11:55:58 2020: ncap2 -O -s *var_tmp=iareafl(0); iareafl=float(iareafl-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 11:55:58 2020: ncap2 -O -s *var_tmp=iarea(0); iarea=float(iarea-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 11:55:58 2020: ncdiff -O /home/hgoelzer/Projects/ISMIP6/Archive_sc/Data/SC_GIC1_OBS0//AWI/ISSM1/expb01_05/scalars_mm_GIS_AWI_ISSM1_expb01.nc /home/hgoelzer/Projects/ISMIP6/Archive_sc/Data/SC_GIC1_OBS0//AWI/ISSM1/ctrl_proj_05/scalars_mm_GIS_AWI_ISSM1_ctrl_proj.nc anc_cr_tmp.nc      NCO       "4.6.0"    history_of_appended_files         �Wed May 13 11:55:59 2020: Appended file /home/hgoelzer/Projects/ISMIP6/Archive_sc/Data/SC_GIC1_OBS0//AWI/ISSM1/expb01_05/scalars_mm_GIS_AWI_ISSM1_expb01.nc had no "history" attribute
          smb                 comment       9Surface Mass Balance flux (for areas covered by ice only)      coordinates       lat lon    	long_name         surface mass balance   units         kg s-1          x   sle                 comment       The thickness of the ice sheet     coordinates       lat lon    	long_name         sealevel equivalent ice mass   units         m           |   limgr                   comment       The thickness of the ice sheet     coordinates       lat lon    	long_name         grounded ice mass      units         kg          �   limfl                   comment       The thickness of the ice sheet     coordinates       lat lon    	long_name         floating ice mass      units         kg          �   limaf                   comment       The thickness of the ice sheet     coordinates       lat lon    	long_name         ice mass above flotation   units         kg          �   lim                 comment       The thickness of the ice sheet     coordinates       lat lon    	long_name         ice mass   units         kg          �   ivolgr                  comment       The thickness of the ice sheet     coordinates       lat lon    	long_name         grounded ice volume    units         m3          �   ivolfl                  comment       The thickness of the ice sheet     coordinates       lat lon    	long_name         floating ice volume    units         m3          �   ivol                comment       The thickness of the ice sheet     coordinates       lat lon    	long_name         
ice volume     units         m3          �   ivaf                comment       The thickness of the ice sheet     coordinates       lat lon    	long_name         ice volume above flotation     units         m3          �   iareagr                 comment       �Fraction of grid cell covered by grounded ice sheet, where grounded indicates that the quantity correspond to the ice sheet that flows over bedrock    coordinates       lat lon    	long_name         grounded ice sheet area    units         m2          �   iareafl                 comment       @Fraction of grid cell covered by ice sheet flowing over seawater   coordinates       lat lon    	long_name         floating ice sheet area    units         m2          �   iarea                   comment       RFraction of grid cell covered by land ice (ice sheet, ice shelf, ice cap, glacier)     coordinates       lat lon    	long_name         ice sheet area     units         m2          �   dx               axis      x      standard_name         projection_x_coordinate    units         m           P   dy               axis      y      standard_name         projection_y_coordinate    units         m           T   oarea                       X   rhof                    `   rhoi                    h   rhow                    p   time                standard_name         time   bounds        	time_bnds      units         days since 1990-1-1 00:00:00   calendar      365_day    axis      T           �E�@ E�@ B����� @�@     @�p     @�@                                                         @     J�0.�w��%[/��f�%W��%���:5��$�:��:PJ�������    @�?�    J�1��*�f�"ޱ����E�x��7E��0 ���<���"ʰ�Q�@��     J$���Nr��G=ӗ���o�� Q��Ω���e�'��
ZN�N�˒Ԛ@Ĭ�    Jb��E��ׄ�����xr�ׅޘҕ����*Җ��ҋ�O�V�����wz�@�c     Iߝ\��Kװ&Y��4קh�װ���7���	���Ҽa�̟�Ji̚�[@��    JU�#�Í���U�?�K���K�] ���W�2����
``��	q�&����R@��     Hٜ������R�"�8���a�-6M�B��-��$���gKA�3�wD@ǆ�    J�L׻���B��ԛ���<W&�D5T�[k)ϯQk�\���S�J�n�J���wD@�=     J�bC�Q��Q�ԢP��H_*�S%N�l+�϶���m���ay&�,�A�r��,��@��    J1�U�,a��du�����X���f��Ӏ�/���Ӂ�]�s���N��˯�%�d�&@ɪ     H���E�Z؂=��l���x�?؄HӒ�YЅHvӔ�{Ӌ��o#�V��͒j�@�`�    J��j�kHxؚgQ�xITؓ�l؜W�ӭ�Ћ��ӯ��Ӧ}a͖����͢��@�     J��S�~�ئ��ՅH(؟�ب��ӻ}AЕ��ӽ�+ӳ��͸�J��
�Ƀ@�̀    J�P��ɣخ���Kͱا �ذK+�ĖK�eU���`�ӻ����b̸Qy�;2@̄     �z����$���J�M�Mؽ����_��ߪ��gs���y���p��=��ާ,�.�@�:�    J����{���5�G����o���i�^�a l��^��-P�9#������X�c@��     �mP�������D�T��2��yO������sO���������l>$�>��u�@Χ�    ����Є��
L�Tj2y���
���O�Ġ�^����U�`̨��k@@�^     J�y����b��#S��:�)����1� N���1��(�w�f̹s��}K�@�
@    ɲ���J*�!5��Az6��X�!�[�5g��Y��6A��,'��v�~�	�Ώ$�@�e�    Jg��h��,J��-�%ER�,���A��B�^�B���9���X���<�΄s@���    Io��	`��3i��4M��,��4:�I���J���J���Bl�U���;�r\c@�     J40ż��CL��V��;Z��D"��[���p�Z�\���R�G�y���DZ΋H%@�w@    �V>f��6�K���`N��C�;�L�*�e`�|h��f\v�\f�΂�8��RTΒ�]@�Ҁ    H�`μ--�bb�|�|�Y�L�c_�~�FЎO�����t��Β�v� �\Χa@�-�    J[�ü8&�p�ո��g�c�r?ԇZ��)�Ԉ)6ԂE�Η�e�a�γ��@҉     �n'��?��y�4պ��pM��{,ԌE��X�ԍQ�ԇ4&Τ2�̓;����@��@    Ihm�Qg�و����ك��ى]�ԙ����? Ԛ��Ԕ-�ε{�́3���g@�?�    J|$�[*�َ�y����ى�ُ�Ԡ�����ԡ�yԛκ<x͐D���M�@Ӛ�    JD�_�%ّ�R����ٌ�|ْ~ԣ��|�Ԥ�ԞOQμ	�͋0�����@��     J�|-�j�Wٙ�����ٓ�8ٚ�ԬFn�	ϛԭZԦ"��L͕��P�@�Q@    I�I�n0xٛ�3�|�ٕ�Gٝ!,ԯm��17P԰�_Ԩ���� �P����v@Ԭ�    I�~�w�١���,�ٛ^�٢�-Ե�k�*�Է�Ԯ�>��nG�:'|���7@��    �|
���i�٨	����١�X٩3^Խ��'}?Ծe�Ե����;�<~Y�W@�c     ��ʼ���ٱ�0���٪�|ٲ���� 7�+���W�Կ�+� �;�Dx�<�@վ@    JO�2��~�پ���Jٵ��ٿ���֓N� �c���5��~���	͎]|�ù@��    ��Ox��'~��}3��ٻ�g�ƃ=��:��n���a���f��$͍
���z@�t�    Ii?����������!��@'��O	��B��2�-�짵����Z͵K��%��@��     ��Jb�������,>���l���+���\��AҶ������,�D�ͼ���0�L@�+@    ɽ-�������p�+Ӡ��������O��AZ*����HO�%�ͩy5�;.@׆�    J�Η��=�����-����2��������Ca5��?� ���,��ͫ�6�B#A@���    �W缹����*�+����˝����
,��A���
�����6Ɖ͡���Kh@�=     �X����j�� ��/����A�� ��!B�E�������o�;��̤ͤ�PI9@ؘ@    ʪwt���<����4܃� �B�ch����K���ym����H�ͭ�k�]��@��    �8"��N�6��7��?���Y� ��N�y� �2�1{�H�Cʹ���_@�N�    ������9����#�����|��&���6r�'��bz�Q-��u��`�_@٪     ʻ��q��յ�@�k��Dg�/q���Im�/���'��Vv�ͯ�I�lm+@�@    ��¼�P �#���띰�&�$2��8@����8Ĩ�/���[$��<�vĥ@�`�    ʺ;�����+F������#.�+���@���
%��AE��7���a�s��!��}��@ڻ�    ��]��l�2���  ��*��3��H���-��I���@"��m�K��_φ�@�     ʄLC�l=�;���	���3�<��S	B�@j�S���I���yg��-OϒV@@�r@    �,?��K�B�\����:	��C)��Z��#��[���QXRρ�y�A �ϙ�@�̀    ʻڡ��+�Lޖ�{��D��M`�f����,�g��\��ψ6��>W�Ϡ�@�(�    ��c�!���TLI����K`��T�'�n���b��oy#�d��ύ-��@N4ϥ7{@܄     �͔��&���Z�K��S�Q�;�[k��vc[�i��v���k�bϐ��>��Ϩ�,@��@    �ҽ��-'Z�c�F�1��Y�b�dwՀ� �ՀX	�u_ϕc�H�{Ϯ4R@�:�    �V½1�H�i{ ��@�_���j�Ճ]x�*|Ճ���{��ϗ��L�ϱ%X@ݕ�    �k߽:"]�t�`�{�j��umbՉ�3��IՊ)Ճ�Ϟ���OuVϸ��@��     ˂��B��~�+�XW9�t����ՏH�sqXՏ��ՉP�ϟ��gw�ϻ��@�L@    �>�սM�Oچ�"�U�NځD�ڇ&�՗�!�pB�՘BՑvqϦ���f��ë�@ާ�    �+Gn�V�"ڌ��K/�چ��ڍ�՞L��d�՞��՗�/ϫ��f]i��j�@��    �O�H�^�ڑ���Uc$ڌ�ڒH�դ#��p�դ��՝�7ϯE�^���!�@�^     �۶νg��ڗ���Vz�ڑ�ڗ��ժ� �qYrժ��գ�ϵ[H�_����Xb@߹@    ���ni�ڛ��7q
ڕ�(ڜW�կ�{�Nlկ��ը�8Ϻ���[Z���PF@�
@    ʯ��u�lڡg�I��ښ��ڡsTյ;��c$�յ�ծϾ���m?`�ܕ�@�7�    ˠ-��|X�ڥ��\C�ڞ�zڥ�չ�{�w��պ;iղ���·��ks��&_@�e�    ˝X6����ڬ���^S�ڦJڭ'��;��z.�¸�պ�`��r@�[U�����@��     ˶�̽��Vڴ ��UHڭd�ڴ�G�ʱ��o���)b�����2�V���	�@���    ˴�����ڼ��Y2[ڵ�ڽ@���{��tg������̽����^���I@��`    ː�g��W���~�ֆ��ھWO�����<�ї�}���O��/��ب��o ����@�     ˎ�X���̲O֍�5��~���@"��V�џ��������<Q�ݯ)Ά����T_@�I�    ˖�Y����Ԏ�֌����+��h��/�ў:J���������j�΋�k��@�w@    ��G����v����֕���j��܄���|NѨ����%�����4Ό���9\@��    �V����{���֚D���^)��$� ��ѭ�o�7�������UΒ5��	0�@�Ҁ    ��O#���1��b֕{��㘇�����opѨ5��Ë� ���4�Δ2� �@�      ���:���j��I�֔<��`F�����	rѦ���	�j��w��^{ΏEx���@�-�    ˾>Ƚ�vO���k֮"������\��*��������	�����Ύ�[��@�[`    ��������]f֪5>��������>ѿ���������Ί�`�1@�     �!D��
���־L���P@�ػ��"��C��6���ONΐ�4���@ⶠ    �r9��h��PNִ$F�%��`��6�ʵz�I��"|�
U΍|���@��@    ��y���>��Q�ְ�#�|��,�#�C���u�#������_Έ^���4@��    ����8���0֬%�����C�)[������)���$R��K�·?��3�@�?�    ����4���֣���}���/�Ѹ>{�/l�)�����Α1Z�@�m     � ���0�� ���h&��F� ���4ԑт���5��/���
~�΄s��@��    ��p� aH�&Hւ���!u��&\��:�`ѓA��;4�5����8Έh��%@��`    