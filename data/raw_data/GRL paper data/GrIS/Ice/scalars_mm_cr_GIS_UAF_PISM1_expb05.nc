CDF   V   
      time             nco_openmp_thread_number            Description       PISMIP6-Greenland recalculated scalar output. Heiko Goelzer 2019, h.goelzer@uu.nl   history      �Wed May 13 12:16:05 2020: ncks -A -v oarea,rhof,rhoi,rhow,dx,dy /home/hgoelzer/Projects/ISMIP6/Archive_sc/Data/SC_GIC1_OBS0//UAF/PISM1/expb05_05/scalars_mm_GIS_UAF_PISM1_expb05.nc anc_cr_tmp.nc
Wed May 13 12:16:05 2020: ncap2 -O -s *var_tmp=smb(0); smb=float(smb-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 12:16:05 2020: ncap2 -O -s *var_tmp=sle(0); sle=float(sle-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 12:16:05 2020: ncap2 -O -s *var_tmp=limgr(0); limgr=float(limgr-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 12:16:05 2020: ncap2 -O -s *var_tmp=limfl(0); limfl=float(limfl-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 12:16:05 2020: ncap2 -O -s *var_tmp=limaf(0); limaf=float(limaf-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 12:16:05 2020: ncap2 -O -s *var_tmp=lim(0); lim=float(lim-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 12:16:05 2020: ncap2 -O -s *var_tmp=ivolgr(0); ivolgr=float(ivolgr-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 12:16:05 2020: ncap2 -O -s *var_tmp=ivolfl(0); ivolfl=float(ivolfl-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 12:16:05 2020: ncap2 -O -s *var_tmp=ivol(0); ivol=float(ivol-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 12:16:05 2020: ncap2 -O -s *var_tmp=ivaf(0); ivaf=float(ivaf-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 12:16:05 2020: ncap2 -O -s *var_tmp=iareagr(0); iareagr=float(iareagr-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 12:16:05 2020: ncap2 -O -s *var_tmp=iareafl(0); iareafl=float(iareafl-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 12:16:05 2020: ncap2 -O -s *var_tmp=iarea(0); iarea=float(iarea-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 12:16:05 2020: ncdiff -O /home/hgoelzer/Projects/ISMIP6/Archive_sc/Data/SC_GIC1_OBS0//UAF/PISM1/expb05_05/scalars_mm_GIS_UAF_PISM1_expb05.nc /home/hgoelzer/Projects/ISMIP6/Archive_sc/Data/SC_GIC1_OBS0//UAF/PISM1/ctrl_proj_05/scalars_mm_GIS_UAF_PISM1_ctrl_proj.nc anc_cr_tmp.nc      NCO       "4.6.0"    history_of_appended_files         �Wed May 13 12:16:05 2020: Appended file /home/hgoelzer/Projects/ISMIP6/Archive_sc/Data/SC_GIC1_OBS0//UAF/PISM1/expb05_05/scalars_mm_GIS_UAF_PISM1_expb05.nc had no "history" attribute
          smb                 
_FillValue        `�x�   cell_methods      
time: mean     comment       %positive flux corresponds to ice gain      coordinates       lat lon    	long_name         surface mass balance   missing_value         `�x�   pism_intent       
diagnostic     units         kg s-1          L   sle                 
_FillValue        `�x�   coordinates       lat lon    	long_name         sealevel equivalent ice mass   missing_value         `�x�   pism_intent       
diagnostic     units         m           P   limgr                   
_FillValue        `�x�   coordinates       lat lon    	long_name         grounded ice mass      missing_value         `�x�   pism_intent       
diagnostic     units         kg          T   limfl                   
_FillValue        `�x�   coordinates       lat lon    	long_name         floating ice mass      missing_value         `�x�   pism_intent       
diagnostic     units         kg          X   limaf                   
_FillValue        `�x�   coordinates       lat lon    	long_name         ice mass above flotation   missing_value         `�x�   pism_intent       
diagnostic     units         kg          \   lim                 
_FillValue        `�x�   coordinates       lat lon    	long_name         ice mass   missing_value         `�x�   pism_intent       
diagnostic     units         kg          `   ivolgr                  
_FillValue        `�x�   coordinates       lat lon    	long_name         grounded ice volume    missing_value         `�x�   pism_intent       
diagnostic     units         m3          d   ivolfl                  
_FillValue        `�x�   coordinates       lat lon    	long_name         floating ice volume    missing_value         `�x�   pism_intent       
diagnostic     units         m3          h   ivol                
_FillValue        `�x�   coordinates       lat lon    	long_name         
ice volume     missing_value         `�x�   pism_intent       
diagnostic     units         m3          l   ivaf                
_FillValue        `�x�   coordinates       lat lon    	long_name         ice volume above flotation     missing_value         `�x�   pism_intent       
diagnostic     units         m3          p   iareagr                 
_FillValue        `�x�   coordinates       lat lon    	long_name         grounded ice sheet area    missing_value         `�x�   pism_intent       
diagnostic     units         m2          t   iareafl                 
_FillValue        `�x�   coordinates       lat lon    	long_name         floating ice sheet area    missing_value         `�x�   pism_intent       
diagnostic     units         m2          x   iarea                   
_FillValue        `�x�   coordinates       lat lon    	long_name         ice sheet area     missing_value         `�x�   pism_intent       
diagnostic     units         m2          |   dx               axis      x      standard_name         projection_x_coordinate    units         m           $   dy               axis      y      standard_name         projection_y_coordinate    units         m           (   oarea                       ,   rhof                    4   rhoi                    <   rhow                    D   time                standard_name         time   	long_name         time   bounds        	time_bnds      units         days since 2008-1-1 00:00:00   calendar      standard   axis      T           �E�@ E�@ B����� @�@     @�p     @�                                                         @�     I����D���pS����ʽ��*o� ��OD&�����ޑ��*�K�0���@���    J�5�x՜�)T�ç�1Z��k"�аpO�GЄK��G�q�P�K�\��1%@��     ʁݯ�#�)�U��T%���N��ShV�p��O:��m�?�g�-�N�L�G��f�@�z�    �hi뺔rf��FSTl��׺��׾m*��\�O����H4���:0	L3��.�	@��    J���׼��TW�@׶f�׻!��xVOs�ҒP��@��P\�LRn�C5�@Ȝ�    �_?��k��	�vS������	���(wN�^��H�O�Ώ@Lsw�·y�@�.     I"Lк�e�`�T�6�2����&�:O/Nr�&G��!	Φ�&L��Μ.�@Ͽ     H��Y��љ�"|cT�� �wl�!iI�6�]O��M�5���0[��N�L�PIη��@Ѩ     ʾ���+/��_�T�|W�WK��]��z�P���x���rD����L�q��݂�@�p�    I�Z�2I:�g6�T|�0�`9��f9�ӂ�O�CӁ���|P���3L��/���@�9@    �ŴƻC&؀�sTںn�uo؀ �ӑ#�O�!Ӑ-�ӊ��L�_i��@��    ʉ���k�؜IT���ؔXn؛�ӯ�mPEӮ��Ӧ���(��L���#p%@��@    J
wػj��؛���boؓ��؛J{Ӯz>���Ӯ��Ӧ8�/�K�j��-m@ڒ�    ʏw|����ض�4Ԍ�@خʊطP�ͨvϞ����G�İ&�F���J��HU@�[�    ��
���Z��%0ԗ�����ݼ����dϪ�������p�\\��O�O�_��@�$     �7x������!�}����*����#Ύ������h>��?��k>@��    ��0��=�� ?�T`�S����� ��P�O|��w�
'��i�� ��π��@�ڀ    �D-��W��	Y}T�̪����	��UO����8]�"mτ�?�e φ�c@��    �-_J� ��*&zS��a�!
�*
[�?wAN�. �?W��56�ϠH)�c�ϧey@�     ʎ�b�l|�;,�Շ�Y�0��<;��R�PИ���SЛ�F�ZϬ�<�ğ|Ϲ4@�@    �)]�ܰ�Q���rs��F��R{0�kȑЈi��l�d�_i9ϸX�ͷk����@�k�    ʣ2޼*��b�:ոAk�V��d��~����V�ԀO/�qw������؎��J�@�O�    ʌZ�6
��q������d�6�s}�ԇ���=ZԈ�RԀ�������p���u�@�4     ʂ���Aj�ـ}��Ȥ�sA�ف�Ԑ�C�J�ԑ��Ԉ�p��p<�����@�`    ʕ �M|Rو_����ف7�ى\�ԙt����Ԛ�ԑg���N���o���@���    �"ͷ�c{ٖ� ��+Pَ�[ٗ�Kԩ����`�Ԫ�]Ԡ�������j����@��     �'Sy�k�Uٜ�R��S�ٔNBٝ��԰w���eԱ[PԦ�y�������
�@��@    �~��}3A٨���y�ٟ8�٩ ZԽ#O�|�Ծ,HԳ+�	���ݧ����@ꩀ    ����ٵR�ղ�٫�]ٶ���	���p-���"��j���ͼ�a��z@��    �{X�����ٹJ�Ց�ٯ{�ٹ܌�Ё,Ф~��%0��w��l�ͨD����@�r     �������Z�զ��ټ�������TEл�
�����q��!�ͬ�^�&tK@�V`    �%eӼ����՞�՗����Lo��6���a�Ъ�������7�)�&͢^��.�@�:�    �W1#���F���U�ɤ��ۂ�����������|��?�4R�ͯ�<�9ѻ@��    ������M�����+����(��� �A9�	J��f}�<CY͵E�A�S@��    ��몼�����ڔ�Z��������J������h��V�D
�Ͷ��I��@�s�    �Գ���9���G��R�����5�F��a"������LIY�İ��Rn�@���    ��a��x���Y��_�����
������������P�Lͺ"B�V�^@�X     �ǳ��ϾL�
t%�:k���
_��f�)I�ur� ��W}���Ͽ�]�@��     �*�^�����������	���`M�$0'�z��$������`��Ͱ��fz/@�<@    �w���p�����j��G��h��,���,���"[�iv`Ͳ���o�@�`    �JB��F�� �<�C��� �7�4�o�\v��4��*��s`=͢Æ�xvY@� �    �*�ȼ���(�4S�R�����(��=�:N�&��=��2`V�|�3͂��ЀT�@�    ˖9�8��5�UD��*��4�J�K��P]���KyK�?^�Ѕ��dufІ�o@��    �1�����<�YU�F��16��</6�T-gP���S�Y�Gj,Љ �� �/Њb!@�v�    ˉ��t�G6�U���;yn�F���`+�Q�r�_���R��Ў}��V]Џ�C@��    �/�~����N�?V���B�	�N��hoQ_��g��Z��В����p�Гb%@�[@    �<�Խ!V�W0|U�	�J��V���r%�Q	ݼ�q���c�З�����ИQ�@��`    ˒���)���bA�VH�UHo�a���~��Q��~��p }Л�r� ?�М4�@�?�    ˋWO�28�mU�U�b�_���l��Յ��P�8ՅL��{�OС�>�+kDТ�@���    �.�/�7�C�t��U����f���tV[Չ�(P��vՉy+Ձ��Х�@JD��Х�@�#�    �i$'�?*�~��U����pA��~]�ՏNP�r#Տ�Շ-NЪ��%XЫ=�@���    ː"!�G��ڄ��U�v8�z�/ڄ��Օ�Q
!Օa�Ս7�б4FLMNаͷ@�    �"c�Od�ڊ;�U��Hڂj�ډ�՛��Q�2՛H�Ւ�?еߞLo)�еh	@�z8    �fy:�V�0ڏ)AV��چ� ڎ��ա{Q'�JՠĴ՗�л��L��л�@��`    ˥��`!�ڕX2U�C�ڌ�Rڕ�ը�Q	��էȺ՞�e��w	L������)@�^�    ˣ���i^ڛS2U�g�ڒ�ڛ�ծȅQ�ծ��ե"Y���M���Ym@�Р    ˪�a�r�rڡ��U�iژ�Lڡe�յ��P�յ��ի����M'��ʼ�@�B�    ˧��|� ڧ��SP�0ڞ�!ڧ�!ռ�
Nj��ռ�5ղ���'�L��1�цE@���    �݌����ڰԷ�!ڦ�xڰ(���-�ΚO��9�ջ�`��t�L��U���*@�'     ��4b��p�ڷ�x�poڮ%ڷ�����,�G��������k�Lł4�ަ8@��     ˡ����ھH՚/_ڳ��ھ)����Э�#���n�ʁT��*�L��D��M�@�H    ��i\�����[n��h�ڻ��ŏ�����DF��N���u���W�L����f@�}p    �г׽�~j����	����M���.l��2�������ڤ����}L�@����<@��    ˨�t��bm�ӍT�����t,��ٙ����+����c��������L�R���1�@�a�    ��i������g�SZ��Я��܈�����m����(����!��sjL������@���    ��\x��i*���]o����0���� ���y-� ��� 6�ZL&t2��@�F     ��_꽲���օN��ऎ��;P�.�і��y������9�J�ѧ�3@��     �2]������T־����=����
j��֓=�
���q��	������
�@�*@    �G���������������X������m��������ZN�����U�)�@��h    �(d��Ɏ"�+�����}���������]t�����B�L��bSA H    �����ߘ�	A��������	�j�so�x����#��0͋[E��A @X    ��W���:�l~����ˆ��V� D�"�� ��΄�k�͠�����A yh    �	�ν�,�����L�W[����%���'�0�&)-��&�*�͟M�i�A �|    �H۬��h!����&L���]�H��,��;"@�-���%){�)G͵��� ��A �    ����n'��8�7�q�����2�+�N�-�3�	�*���#4Q��l<�$�*A$�    �߯�����#���I?���I�$|�84��bv�9 �00��&z/��q��(iA]�    �S���4�*~?�QӲ�#HS�+P�?��l��@�!�7���*�����9�,��A��    ��-��[�/�+�Tv�(5��0U��E}��o��Fl��=H��-�"��~�/�A��    ��þ	���4R0�Q4�,���5#B�J�$�kC/�K�g�B���0���|r�2��A�    �W5��p�;+4�Rk�3���;���R���l�;�S���J%��5a�Ϳ:��6�AA�    �J�ݍ�A�/�MS�9�s�Bh��Y�3�g��Z�?�QCu�9 4ͬ�P�:y�A{    �(��Y�F�;�P@��?B��G�|�_�!�jWy�`�y�W8��<(w͜�!�=bA�     �Q]g�3t�M�|�S˯�E�+�N[H�gF��nT
�h54�^y��?�͛ku�A&�A�0    �%l��!B�R�@�X:x�J�i�S�{�m�sP��nk�d7��B��͖*�D"BA&@    ��$&�%K��W��]���O�Z�X�D�r��y\��s�j�i�e�E��͐��G�A1�    