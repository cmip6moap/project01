CDF   V   
      time             nco_openmp_thread_number            Description       PISMIP6-Greenland recalculated scalar output. Heiko Goelzer 2019, h.goelzer@uu.nl   history      �Wed May 13 11:56:10 2020: ncks -A -v oarea,rhof,rhoi,rhow,dx,dy /home/hgoelzer/Projects/ISMIP6/Archive_sc/Data/SC_GIC1_OBS0//AWI/ISSM1/expb03_05/scalars_mm_GIS_AWI_ISSM1_expb03.nc anc_cr_tmp.nc
Wed May 13 11:56:10 2020: ncap2 -O -s *var_tmp=smb(0); smb=float(smb-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 11:56:10 2020: ncap2 -O -s *var_tmp=sle(0); sle=float(sle-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 11:56:10 2020: ncap2 -O -s *var_tmp=limgr(0); limgr=float(limgr-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 11:56:10 2020: ncap2 -O -s *var_tmp=limfl(0); limfl=float(limfl-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 11:56:10 2020: ncap2 -O -s *var_tmp=limaf(0); limaf=float(limaf-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 11:56:10 2020: ncap2 -O -s *var_tmp=lim(0); lim=float(lim-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 11:56:10 2020: ncap2 -O -s *var_tmp=ivolgr(0); ivolgr=float(ivolgr-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 11:56:10 2020: ncap2 -O -s *var_tmp=ivolfl(0); ivolfl=float(ivolfl-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 11:56:10 2020: ncap2 -O -s *var_tmp=ivol(0); ivol=float(ivol-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 11:56:10 2020: ncap2 -O -s *var_tmp=ivaf(0); ivaf=float(ivaf-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 11:56:10 2020: ncap2 -O -s *var_tmp=iareagr(0); iareagr=float(iareagr-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 11:56:10 2020: ncap2 -O -s *var_tmp=iareafl(0); iareafl=float(iareafl-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 11:56:10 2020: ncap2 -O -s *var_tmp=iarea(0); iarea=float(iarea-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 11:56:10 2020: ncdiff -O /home/hgoelzer/Projects/ISMIP6/Archive_sc/Data/SC_GIC1_OBS0//AWI/ISSM1/expb03_05/scalars_mm_GIS_AWI_ISSM1_expb03.nc /home/hgoelzer/Projects/ISMIP6/Archive_sc/Data/SC_GIC1_OBS0//AWI/ISSM1/ctrl_proj_05/scalars_mm_GIS_AWI_ISSM1_ctrl_proj.nc anc_cr_tmp.nc      NCO       "4.6.0"    history_of_appended_files         �Wed May 13 11:56:10 2020: Appended file /home/hgoelzer/Projects/ISMIP6/Archive_sc/Data/SC_GIC1_OBS0//AWI/ISSM1/expb03_05/scalars_mm_GIS_AWI_ISSM1_expb03.nc had no "history" attribute
          smb                 comment       9Surface Mass Balance flux (for areas covered by ice only)      coordinates       lat lon    	long_name         surface mass balance   units         kg s-1          x   sle                 comment       The thickness of the ice sheet     coordinates       lat lon    	long_name         sealevel equivalent ice mass   units         m           |   limgr                   comment       The thickness of the ice sheet     coordinates       lat lon    	long_name         grounded ice mass      units         kg          �   limfl                   comment       The thickness of the ice sheet     coordinates       lat lon    	long_name         floating ice mass      units         kg          �   limaf                   comment       The thickness of the ice sheet     coordinates       lat lon    	long_name         ice mass above flotation   units         kg          �   lim                 comment       The thickness of the ice sheet     coordinates       lat lon    	long_name         ice mass   units         kg          �   ivolgr                  comment       The thickness of the ice sheet     coordinates       lat lon    	long_name         grounded ice volume    units         m3          �   ivolfl                  comment       The thickness of the ice sheet     coordinates       lat lon    	long_name         floating ice volume    units         m3          �   ivol                comment       The thickness of the ice sheet     coordinates       lat lon    	long_name         
ice volume     units         m3          �   ivaf                comment       The thickness of the ice sheet     coordinates       lat lon    	long_name         ice volume above flotation     units         m3          �   iareagr                 comment       �Fraction of grid cell covered by grounded ice sheet, where grounded indicates that the quantity correspond to the ice sheet that flows over bedrock    coordinates       lat lon    	long_name         grounded ice sheet area    units         m2          �   iareafl                 comment       @Fraction of grid cell covered by ice sheet flowing over seawater   coordinates       lat lon    	long_name         floating ice sheet area    units         m2          �   iarea                   comment       RFraction of grid cell covered by land ice (ice sheet, ice shelf, ice cap, glacier)     coordinates       lat lon    	long_name         ice sheet area     units         m2          �   dx               axis      x      standard_name         projection_x_coordinate    units         m           P   dy               axis      y      standard_name         projection_y_coordinate    units         m           T   oarea                       X   rhof                    `   rhoi                    h   rhow                    p   time                standard_name         time   bounds        	time_bnds      units         days since 1990-1-1 00:00:00   calendar      365_day    axis      T           �E�@ E�@ B����� @�@     @�p     @�@                                                         @     Iz�/8��VU���\��U�Q�U��P̛V�x�qP���P�)JUe�ʯ���@�?�    ʻ9C/VW'�T��)VuT�VpB�QrO��Q�-�Q�I�B�fJ�ʔ�@��     ʴ�����w��s��&��0��ĨT�� �%f��K3��Do����"ʰˎ'U@Ĭ�    IBC��@��r�]�9�v�r��u�;҈�}�QCyҊ5҈~�C�Uʰ��ˎ'U@�c     ʥ��8e�yz��Q(��g��|��Ҍ]��k\�Ҏ4�҂z��S��Kh��3]�@��    ɘ�ۺ�����Ԍe������F��s\ϝ�K������ݵ�|�.J���t&�@��     ɼݺ��O��TӄU��K���9�����Δ�������	���3L*�̦m�@ǆ�    ��R�ś;���Ԯ����E����ҟ����Zh��D�^�K���I�g@�=     �c�J�]Z�FQ���yD�>^�G���_*2��W��a��V78͝�L�Y͋��@��    �����*�[�b=����V�-�d:��~���p�Ӏi5�q�m����L1��ͼ��@ɪ     ʿ�=��y�	�
J@�ne��|"2ӌ����BӍ�ӆ!���MDL0%��H�@�`�    I��4�o%;؝4Pԟ�ؖb1؝�jӰ��ϳ�ӱ��ө9���Le���+m@�     �ō�tF�ؠ��Խv�ؙ�CءeӴ����2�ӵ��Ӭڙ�'w)L_p��'@�̀    �����ؽ� ���ضؽ�Z�ն��-���̣��ۆ�8��L�+W�%�@̄     ʛ-[��(�������������D	�s��D������r�L�)��V>�@�:�    �S�3��?��|TmW� p�l��lO E�C���·q/Mp��hF"@��     ʐӇ�ݬr��1U.
�e��A!�&wPC�I�%����	Ι�M^�d�|�@Χ�    �XQջ��y�"V�U3#��JB�!���6�-PI���5��,~R΢M>�ΊX!@�^     ��
�Q��ARU&g��6���@���Y��P;@,�Xΰ�M�MΫ��M=�Δ@@�
@    �.�
� N�T������I�y�UG��oe��p�o���b�6ιO�L���άo�@�e�    ��r�4A��o�$�%GM�b�C�p�kԇ��9��ԇa���ο9BL�P}δt:@���    ʿo��E,_ق���V���w��ك)Cԓ��q�3ԓ��ԋ������L� ���؊@�     ʱ�-�P�0يO�՝�gك`�ي��ԛ��б�ԜULԓ�2��L"`��@�w@    ��j��]�ٓ$�է��ً�B̙ٓԥ��м��ԦP�ԝ���P���@���t�@�Ҁ    �E8�kǶٜh<՟��ٔDpٝ�԰ Dг��԰��Ԧ�k��6Q�#���e@�-�    ʆ�n��٨���~3٠�X٩�Ծ	��؛�Ծ�<Դ�2��
��2L���?@҉     �&8�����ٯk�շ9�٦��ٰ"���e���-���3�Ի��vK�R2���z@��@    �8�\��!ٹ���ʃ�ٱ~�ٺ���)����L����Ǻ��(@�MJ����@�?�    ���(��UE��r���M;ٽ���b?��/3�����<{���|����E��Z�@Ӛ�    �D�n��h�ɞZ�֢����x��t����T�������������+e�hX@��     �D�AU���<�L��Ri�����p�_#���.��'��0ͪt��%;�@�Q@    �w�伮���䈈�"gD�۩���V� ���6���K���-���sͱ�i�-�@Ԭ�    ��*���^����'���(O��jd�	W��<���
y�N��!�Mͧ�U�6�8@��    �V���p���B������̛� .M��}��*�=�
K��0�B�����N��@�c     ��ɼ˃������}���@��N����<��;��d�9�{�7'�\�E@վ@    ʇ���4&�	�~�2q���
���I"�H[��~�sj�C�,�	d��fLM@��    �+hr�ך)���@����%��;����X֘�a���2�H�>�S��m�'@�t�    �PZ��ۤ�����P��
��T��!~q�j��"iH�lq�Hl��,���s�	@��     �=���浸��S�e��6��X�)�6р�,�*���#@��K�I�=��{�@�+@    �2�ͼ�K�����j.��]L�r��2e у§�3l��+s��U��I�τ�@׆�    �MG���? �'*Y�Y�z��"�(4�<f�u%�=��3��b%!�T8ϋ��@���    ˱��0r�/e3�	]��'�;�/��E^/���E���<~J�m���9:ώ8@�=     �W�Ľ�F�<-ո���3���<�l�S�����k�T'��JI�|���/�ϔy�@ؘ@    ˤ{4�>��Dlt��$V�;���D��]�� ��]���S7�σ|��@Q\ϛ�"@��    �Z&f����Oh���.��FM��Oג�id����%�i�"�_%�φ�q�G�yϟ�@@�N�    �`9ս#���W�S����N8��W��r�������sC�hcύ�*�?�ϥ��@٪     ˬU��*΂�`����0�VѸ�aC��|�q�_��}{��q�
ϔ�+�B��ϭ4�@�@    ˢui�4���mi����c
�m��Յ����OՅ�>��Dϖ�t�b�7ϳE{@�`�    �UF��>���z�n��L��o��{KՍ��DՍcՆ�`Ϡ�W�{����N�@ڻ�    ˋN��E�ځ���ѻ�x�lڂ#&Ւ+��
N�Ւp�Ջ׺ϥ�_΃a��ƚ�@�     ˫7L�N�ڇaq�9Hځ�Pڇ��՘W%�)՘��Ց�WϭM\Έ�@��ol@�r@    ˔0
�W��ڍ�.�9mڇ��ڎ�՟k��P��՟��՘�;ϱ�Β@��G@�̀    ˆrܽ`Cwړ)��;�Yڍxړ�~ե�/�S>�զ�՞�2Ϻ�s΍hf��K�@�(�    ˾���g�]ژ��)M�ڑܖژrHի,�>�mի�Iդ"j��GΓ�h��5�@܄     ˺��sS�ڟs��W�ڙ~ڟ�ճm)�q�Lճ�'լ.���oΟ*;����@��@    ��o'�~a_ڦ�2�a%�ڟ��ڧ �ջ���}Zռ�մ ���̸ΰ�&����@�:�    ��`���~ڮ��r�>ڧcڮ�,���ш����f�ռ���mγ J� ��@ݕ�    ��5����ڵ���v�ڮm�ڶ;��Q�ъ�������G����Mν���
@��     �񮼽��ھ�֮5%ڷ�ڿ�9���3��
�ׯ;���[������*�	�@�L@    ˶mv��h���u�֗�����L�����hѪ���=e�����A)ξ���t.@ާ�    ��-ɽ��L��XX֙���ǣ=���P��Q�ѭAD���:�९���f����=�@��    ����������5e֬���I:���S��KG�z�����a���ǩ���@�^     ˿}a��(����Wֵ��؅��m��r��� ���8������������r@߹@    �D@��$����ָ�1�����w�������[����b��ra�!�S@�
@    ��,��$���	�ּp��������������	'�����	�>����&��@�7�    � ���.����Sֻ����8?��N+��9��a7���	h:�����2��+��@�e�    ��ѽ�J��O�֭�m��(���p�����_��$��o���J��@��.�]@��     ��q��!��RN֫�N��h���f.��i�ƺ����������2�V@���    �8a�ٵ���	֨%���M���"ѽ6|����������b�7��@��`    ��6��
���֘ے����#R�&\'Ѭ��&�(� �	�������9s�@�     �(X6���\�д֬������'�+����]�,V��&�ͤ��w �>|�@�I�    ��ν�� �<ֶU%�����8�3.���,��3�X�-��&�+���E��@�w@    �\b���e]�$?6֏F���K�$���8Ҫѡ9��9#G�2�^�+����	��H��@��    �(���m�+ս֊O��&'�,��A\�ћ�7�A�\�:���/�8����L^u@�Ҁ    �c���E�1��c��+�r�1���G�Pр��H]�AN��4���~�O��@�      �fG��uQ�7�E�y���1��8��N�<ь���O/��H2'�8G���Tyc@�-�    �(�0�!�?<ց�J�9
S�?D9�V�ђA��W:4�P8��;m&��&��W2@�[`    �"'����D��֎{�>���D��]V
џ��]���V�]�?����֩�[&�@�     �eD����I��֞R��Cħ�J��c�Ѳ(I�ce��\K �?<����\�@ⶠ    �Z�A�!U��P��֢i�J�=�QN�k+%Ѷ���k���dS��@����{�]�6@��@    �5ꎾ&���W��֗�7�Q���W�w�r�tѪ�&�s��kȑ�DKk�ٌ�_|�@��    �_���+f��]�p֍R��W�5�^!�y�Yџ%�y���r���HE���]��d1�@�?�    �-o��0���dz{փ��^ �d�ր��ѓ�Vր���y��I���y�e+3@�m     ̂�5��j6�֍��cƜ�j}!փ��ў�9փ�ր'��LF=��U�gh�@��    ́�ɾ;'��q���v���ka��r{ֈ�ъ��ֈ8�քo%�L����Z�gn4@��`    