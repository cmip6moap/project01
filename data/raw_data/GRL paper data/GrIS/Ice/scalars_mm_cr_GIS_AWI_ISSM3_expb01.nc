CDF   V   
      time             nco_openmp_thread_number            Description       PISMIP6-Greenland recalculated scalar output. Heiko Goelzer 2019, h.goelzer@uu.nl   history      �Wed May 13 11:59:06 2020: ncks -A -v oarea,rhof,rhoi,rhow,dx,dy /home/hgoelzer/Projects/ISMIP6/Archive_sc/Data/SC_GIC1_OBS0//AWI/ISSM3/expb01_05/scalars_mm_GIS_AWI_ISSM3_expb01.nc anc_cr_tmp.nc
Wed May 13 11:59:06 2020: ncap2 -O -s *var_tmp=smb(0); smb=float(smb-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 11:59:06 2020: ncap2 -O -s *var_tmp=sle(0); sle=float(sle-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 11:59:06 2020: ncap2 -O -s *var_tmp=limgr(0); limgr=float(limgr-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 11:59:06 2020: ncap2 -O -s *var_tmp=limfl(0); limfl=float(limfl-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 11:59:06 2020: ncap2 -O -s *var_tmp=limaf(0); limaf=float(limaf-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 11:59:06 2020: ncap2 -O -s *var_tmp=lim(0); lim=float(lim-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 11:59:06 2020: ncap2 -O -s *var_tmp=ivolgr(0); ivolgr=float(ivolgr-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 11:59:06 2020: ncap2 -O -s *var_tmp=ivolfl(0); ivolfl=float(ivolfl-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 11:59:06 2020: ncap2 -O -s *var_tmp=ivol(0); ivol=float(ivol-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 11:59:06 2020: ncap2 -O -s *var_tmp=ivaf(0); ivaf=float(ivaf-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 11:59:06 2020: ncap2 -O -s *var_tmp=iareagr(0); iareagr=float(iareagr-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 11:59:06 2020: ncap2 -O -s *var_tmp=iareafl(0); iareafl=float(iareafl-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 11:59:06 2020: ncap2 -O -s *var_tmp=iarea(0); iarea=float(iarea-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 11:59:06 2020: ncdiff -O /home/hgoelzer/Projects/ISMIP6/Archive_sc/Data/SC_GIC1_OBS0//AWI/ISSM3/expb01_05/scalars_mm_GIS_AWI_ISSM3_expb01.nc /home/hgoelzer/Projects/ISMIP6/Archive_sc/Data/SC_GIC1_OBS0//AWI/ISSM3/ctrl_proj_05/scalars_mm_GIS_AWI_ISSM3_ctrl_proj.nc anc_cr_tmp.nc      NCO       "4.6.0"    history_of_appended_files         �Wed May 13 11:59:06 2020: Appended file /home/hgoelzer/Projects/ISMIP6/Archive_sc/Data/SC_GIC1_OBS0//AWI/ISSM3/expb01_05/scalars_mm_GIS_AWI_ISSM3_expb01.nc had no "history" attribute
          smb                 comment       9Surface Mass Balance flux (for areas covered by ice only)      coordinates       lat lon    	long_name         surface mass balance   units         kg s-1          x   sle                 comment       The thickness of the ice sheet     coordinates       lat lon    	long_name         sealevel equivalent ice mass   units         m           |   limgr                   comment       The thickness of the ice sheet     coordinates       lat lon    	long_name         grounded ice mass      units         kg          �   limfl                   comment       The thickness of the ice sheet     coordinates       lat lon    	long_name         floating ice mass      units         kg          �   limaf                   comment       The thickness of the ice sheet     coordinates       lat lon    	long_name         ice mass above flotation   units         kg          �   lim                 comment       The thickness of the ice sheet     coordinates       lat lon    	long_name         ice mass   units         kg          �   ivolgr                  comment       The thickness of the ice sheet     coordinates       lat lon    	long_name         grounded ice volume    units         m3          �   ivolfl                  comment       The thickness of the ice sheet     coordinates       lat lon    	long_name         floating ice volume    units         m3          �   ivol                comment       The thickness of the ice sheet     coordinates       lat lon    	long_name         
ice volume     units         m3          �   ivaf                comment       The thickness of the ice sheet     coordinates       lat lon    	long_name         ice volume above flotation     units         m3          �   iareagr                 comment       �Fraction of grid cell covered by grounded ice sheet, where grounded indicates that the quantity correspond to the ice sheet that flows over bedrock    coordinates       lat lon    	long_name         grounded ice sheet area    units         m2          �   iareafl                 comment       @Fraction of grid cell covered by ice sheet flowing over seawater   coordinates       lat lon    	long_name         floating ice sheet area    units         m2          �   iarea                   comment       RFraction of grid cell covered by land ice (ice sheet, ice shelf, ice cap, glacier)     coordinates       lat lon    	long_name         ice sheet area     units         m2          �   dx               axis      x      standard_name         projection_x_coordinate    units         m           P   dy               axis      y      standard_name         projection_y_coordinate    units         m           T   oarea                       X   rhof                    `   rhoi                    h   rhow                    p   time                standard_name         time   bounds        	time_bnds      units         days since 1990-1-1 00:00:00   calendar      365_day    axis      T           �E�@ E�@ B����� @�@     @�p     @�@                                                         @     �L ����4d��d3��4���5H��J��΀e%�K���Kq�K�x��t    @�?�    Jp�a��%�Ө�"Q��'@��:�sνs�<4��6�O˵����� �B@��     Jp�]�����M���}��6���$m~����&��� �&���9���3 �@Ĭ�    ��8�^��כu�ʿb׋��ל?�Ү���%�ү��ҝ�[̭�^�*�&��y@�c     Hي0�����Ȟ�͏�׸\C���S�����PB��]3��t���ɺ�A S���@��    ɹ����:��
�"Ԑ��� mh� z�D�Ϣ�z��b���3�LD��BD<@��     H���K�!���q�����"���6�χ�M�7�)�)�#�7̋��iV@ǆ�    �/���/��N;��l[��C,i�O(�h�τ���i��[���(X́�$�iV@�=     I���$<��\�ӓV��N���]��xl!Υ˱�x��hoN�?�-̰
%͋� @��    I��i�6���w��ԛ���e�)�x�VӋe9ϯ8�ӌqӁN��k�M��9rͰX@ɪ     ��`��S�Fؑ(lӑ؅ؑL�ӣW�Σ<6ӣ�~ӕ�{��,���Ò�
��@�`�    �1�%�z}�ب�S�؝��ة�_ӽ�z�'�Tӿ�ӱ@:��.�#�-��@�     I�/f��KTظ�yT�+�ثi�ظM�ϵ#O�;������<�$��� u,�L�@�̀    J�=��S�����T?ص���Ũ8�޷>O0u��k&��A0�E����#�e�@̄     ��>�����۶������B}������=+�"�h���d���9�g͆���|��@�:�    �k���������zԣ����u� H����ϸ$��Z��6��U��͗�ΐ��@��     I�>���(S�RXS_�g�����D[�f9N{�R�V|�W�΁%��w#iΠ
d@Χ�    �N2������iT�����\�C�( �O�4*�'�'�7�|�c�e�Λ@�^     ʳ/��K#�)��T�J�G��)H8�?�P{a�>}&�3;�΂�͖�Χ��@�
@    J��"��|�,�QT�W� ���,}��B�P���B|�4��Έg=͖��ή&�@�e�    ʓ�3�
j�7�[U��G�-�{�6��N�VP����Mׁ�C]`Έ�A͍��άS*@���    �ky�����>v�U�k��4���=5��VR�P����T���K&q΄�̈́�Υ>�@�     �L*�AM�Om'U�5�CB��NY�iibP�Np�h2��[��Ί�͉s�έK|@�w@    Ȍ�'�"U��X��U�>��L*Z�W�g�s�?P�0��r���e�Γ:͂�?γ�@�Ҁ    �1�μ2k@�mdU���`d��k�}ԅ[�P��.Ԅ��|��Εb��t(lγ�@�-�    H�ڜ�?��}upUzF��pBa�|{*Ԏ��P�ЁԎ(ԇ-�Ϋ�B͏�����A@҉     �����G6Sل7@UC-x�z�LكթԔ�tP[��ԔY�Ԍ�*μ�<͛���~@��@    ��D�Y�ِQ�Ux�و��ُՇԢffP�_ԡ�UԚ{�Ѭ�͈a����@�?�    IX\>�cB#ٖm�U�=Sَ�ٕ�ԩF"P��8Ԩ�tԠϴ���8̀3o���@Ӛ�    �B� �h�ٚ�UQ�Wْ\ٙ��ԭY6Pk�Ԭ�7Ԥ�����k�s+� �@��     J	`��u6�٣=UJ:Fٚ31٢��Է�3Pc��Է>kԭ�o���́���+@�Q@    �
��x��٥��U40�ٜ��٥K�ԺffPJÛԺ԰/����x���f@Ԭ�    ��|ݼ���٫� T�{٣V�٫�M��{7OPo��hmԷ�1���k͓#�,Z@��    ʆ�ż��bٳ>Tz�٪{ٳ��ɲ]O��?�ɏ0Կ�j�	���ZC�*�@�c     ʱ[Ӽ���ٽc�S��5ٳ��ٽU3��VOb��*��[ ���^D(�pW@վ@    G"�Y�����ȕ�ԺXWپ�a���U�ᶓ�Ѱ}�������Z�n��x�t�'��@��    ʝ����#��cԿY���
j��D9���m��RB��B�ܙ���4����,� @�t�    �	����c��e-�^�i�� ��ԋ���@�z����^�����$^�}s�3�%@��     ʠ(������sKՅ���4���c��Е�%�c��� M�'*�ͮ45�<�R@�+@    ʖ,ż��V��+�Ր�\��@���f���У8�y�����.��΁��G�&@׆�    J|'A����� �՟ʎ��i����Y�k7г����#��:S���U��U^K@���    ʱB5��$M� w=�/~����� ���.�Ez������]�G:��s��_��@�=     ��?+��=E��s�06:�������px�FIf��
�f`�M�'ͻ�S�ed�@ؘ@    �	w��Ԙ��~#�8�O��v��Q� W��O�� ���o��Y�������r@��    ��.ܼ�L��B��@b��k^�s�'���X|��(+����]�1͸XG�t�:@�N�    �&S���PW��j�2�U�l�(�.e��I0�.���$c��a^�ͧ��v?�@٪     ��3��c�#'N�K�#��#Z�7���d��7���-s�f���S$�JP@�@    �#;�� 0��*Gw�W��!8��*}:�?�`�q���?���5j��l_���(ς1�@�`�    �8�e��2r�^-�)Q�2���H���z^��Iz�>4�s��ͼ;2υ��@ڻ�    �1�ؽɛ�:��՞�y�1��;<��RX{вjO�R���G?$������ύ3@�     ���Y����C����|�9���DY��\q����\��P��ςz��	��ϓ�I@�r@    �a�f�3��K����P�@���K���dt��Ea�e �X�?χ~A�
�ϙߗ@�̀    �冽!���U���o�K%��V%��pfn���p���d��ύ��&
8ϢPV@�(�    ʩG�'�E�]S��Q��R���]��y��eP�y�/�m6uϓ
��$̬ϧ�4@܄     ����+��b�iհ���X5�cJ��`���!$��=�sJ�ϖY��
U$ϧ�4@��@    ʛ��3�i�m),��+z�b��m��Յo��۞�Յ�g�~j�ϟ��0fϵ�@�:�    �H��8���s��խ���h|��tU�ՉG��ñ+Չx�Ղ�nϣr��#��Ϸ�I@ݕ�    �Se�@���~*�Պ�I�r�~o�Տ �Л�PՏ'�Ո9�Ϩ����ϼ�@��     ˜oϽH��ڄt����|5ڄ�&Օj���ՕՍ�ϮS�7����@�L@    �r-ֽS}�ڋ�
՞kڄ�lڋ�՝=_вC�՝i�Օ��ϴ��4���!@ާ�    �^���\�ڑ�z՞#/ڊśڑ�դ�б�դ9g՜(Ϻ$�"����v@��    ˁ��eOڗ e՜�ڐ	ڗGhժЯ�ժ:�բ�Ͼ������B�@�^     �!��n_9ڝRՐ%�ڕ�ڝ7[հ��Т4�հ�Uը����>K��q���y@߹@    �G��u7�ڡx"ճSKښ3�ڡ��յ�����Qյ��խ�-��,�����G�@�
@    ��ڽ}��ڦ�Wձ�ڟpRڧ&�ջ�`��E�ռqճi��Δ�/���䅄@�7�    ˹⹽�P�ګ�[��@�ڣ��ګ����F�� �����9ոl���̔�+�P��E@�e�    ˶���}Pڳ����<%ګ��ڳ����,{� ����l���)���׎�.���@��     �����{�ڻOh����ڳ2�ڻ�e��Ƃ������ɥ������,:/��RD@���    ��a��]�÷`��fڻu����9��<����܀����l��J�0������@��`    ˪Rh�����1j�����û ��o��������� ��@H��t��H7�� ��@�     ˨3��j.�ӟ����������ڶ��"������d���p\���P�G���_t@�I�    ˯�t��+P��1�� z���>��ۂ%�����4�>�����.����O׈���@�w@    �ۺ��>�����������f������-5�����.���j��Mt��	��@��    ˅\���?�롟�:����V������2�R[������a�����XaI���@�Ҁ    �闓��?����(���������x4�=l��z���q�Y	p��@�      �ڴ��������1�l��Z��E`����H����8v�9�YV���y@�-�    ���K��!
�Gp��#��p��n�����1��������ì�S���@�[`    ����ͭy�q���Vw����H��!	x�p���_�	��H�&��u@�     ��ӽ�@��C���^���c\�� ���ٖ��w���=x��h�@ⶠ    �`~�ݚ������ú�ZL����"�����^�"����c�Ky�C����@��@    �cA�����իF��gx��/�(w�����(��"~�����5���Y�@��    �����>���"ҙS��0��o�-��ͬ���-���'���_����u~@�?�    �07��v@���T�8{�[��D�3�!O��8�3���-�E����m��k@�m     ������%�U>���%��9�^PU�Z�9� �3z*���o���@��    ��a����*d�U�ǣ�$���*S��?�RP��6�?��9bH�@w�������@��`    