CDF   V   
      time             nco_openmp_thread_number            Description       PISMIP6-Greenland recalculated scalar output. Heiko Goelzer 2019, h.goelzer@uu.nl   history      �Wed May 13 12:20:10 2020: ncks -A -v oarea,rhof,rhoi,rhow,dx,dy /home/hgoelzer/Projects/ISMIP6/Archive_sc/Data/SC_GIC1_OBS0//VUB/GISMHOMv1/expb02_05/scalars_mm_GIS_VUB_GISMHOMv1_expb02.nc anc_cr_tmp.nc
Wed May 13 12:20:10 2020: ncap2 -O -s *var_tmp=smb(0); smb=float(smb-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 12:20:10 2020: ncap2 -O -s *var_tmp=sle(0); sle=float(sle-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 12:20:10 2020: ncap2 -O -s *var_tmp=limgr(0); limgr=float(limgr-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 12:20:10 2020: ncap2 -O -s *var_tmp=limfl(0); limfl=float(limfl-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 12:20:10 2020: ncap2 -O -s *var_tmp=limaf(0); limaf=float(limaf-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 12:20:10 2020: ncap2 -O -s *var_tmp=lim(0); lim=float(lim-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 12:20:10 2020: ncap2 -O -s *var_tmp=ivolgr(0); ivolgr=float(ivolgr-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 12:20:10 2020: ncap2 -O -s *var_tmp=ivolfl(0); ivolfl=float(ivolfl-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 12:20:10 2020: ncap2 -O -s *var_tmp=ivol(0); ivol=float(ivol-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 12:20:10 2020: ncap2 -O -s *var_tmp=ivaf(0); ivaf=float(ivaf-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 12:20:10 2020: ncap2 -O -s *var_tmp=iareagr(0); iareagr=float(iareagr-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 12:20:10 2020: ncap2 -O -s *var_tmp=iareafl(0); iareafl=float(iareafl-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 12:20:10 2020: ncap2 -O -s *var_tmp=iarea(0); iarea=float(iarea-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 12:20:10 2020: ncdiff -O /home/hgoelzer/Projects/ISMIP6/Archive_sc/Data/SC_GIC1_OBS0//VUB/GISMHOMv1/expb02_05/scalars_mm_GIS_VUB_GISMHOMv1_expb02.nc /home/hgoelzer/Projects/ISMIP6/Archive_sc/Data/SC_GIC1_OBS0//VUB/GISMHOMv1/ctrl_proj_05/scalars_mm_GIS_VUB_GISMHOMv1_ctrl_proj.nc anc_cr_tmp.nc      NCO       "4.6.0"    history_of_appended_files         �Wed May 13 12:20:10 2020: Appended file /home/hgoelzer/Projects/ISMIP6/Archive_sc/Data/SC_GIC1_OBS0//VUB/GISMHOMv1/expb02_05/scalars_mm_GIS_VUB_GISMHOMv1_expb02.nc had no "history" attribute
          smb                 
_FillValue        `�x�   comment       9Surface Mass Balance flux (for areas covered by ice only)      	long_name         surface mass balance   missing_value         D�x��@   units         kg s-1          �   sle                 
_FillValue        `�x�   comment       Ice thickness of the ice sheet     	long_name         sealevel equivalent ice mass   missing_value         D�x��@   units         m           �   limgr                   
_FillValue        `�x�   comment       Ice thickness of the ice sheet     	long_name         grounded ice mass      missing_value         D�x��@   units         kg          �   limfl                   
_FillValue        `�x�   comment       Ice thickness of the ice sheet     	long_name         floating ice mass      missing_value         D�x��@   units         kg          �   limaf                   
_FillValue        `�x�   comment       Ice thickness of the ice sheet     	long_name         ice mass above flotation   missing_value         D�x��@   units         kg              lim                 
_FillValue        `�x�   comment       Ice thickness of the ice sheet     	long_name         ice mass   missing_value         D�x��@   units         kg             ivolgr                  
_FillValue        `�x�   comment       Ice thickness of the ice sheet     	long_name         grounded ice volume    missing_value         D�x��@   units         m3             ivolfl                  
_FillValue        `�x�   comment       Ice thickness of the ice sheet     	long_name         floating ice volume    missing_value         D�x��@   units         m3             ivol                
_FillValue        `�x�   comment       Ice thickness of the ice sheet     	long_name         
ice volume     missing_value         D�x��@   units         m3             ivaf                
_FillValue        `�x�   comment       Ice thickness of the ice sheet     	long_name         ice volume above flotation     missing_value         D�x��@   units         m3             iareagr                 
_FillValue        `�x�   comment       3Fraction of grid cell covered by grounded ice sheet    	long_name         grounded ice sheet area    missing_value         D�x��@   units         m2             iareafl                 
_FillValue        `�x�   comment       @Fraction of grid cell covered by ice sheet flowing over seawater   	long_name         floating ice sheet area    missing_value         D�x��@   units         m2             iarea                   
_FillValue        `�x�   comment       RFraction of grid cell covered by land ice (ice sheet, ice shelf, ice cap, glacier)     	long_name         ice sheet area     missing_value         D�x��@   units         m2              dx               axis      x      standard_name         projection_x_coordinate    units         m           �   dy               axis      y      standard_name         projection_y_coordinate    units         m           �   oarea                       �   rhof                    �   rhoi                    �   rhow                    �   time                standard_name         time   	long_name         time   bounds        	time_bnds      units         days since 1990-12-31 00:00:00     calendar      365_day    axis      T           $E�@ E�@ B����� @�@       �                                                      @�x�    �NHN�EGs�x"�    �x��x"�ҋ�3    ҋ�3ҋ��̑�i    ̑�i@�/     ɖٺ��t��1�    ��-��1����    �������JS�    JS�@��    Ik����ܻ�b�    �^��b��x�    �x��tt�o��    �o��@Ü     ������;2    �;,L�;2�R�s    �R�s�R��̫M�    ̫M�@�R�    ���9.��h��    �h�+�h��Ӄ�    Ӄ�Ӄ	�̬In    ̬In@�	     J��ĻB��t�    �t ��t�ӉR�    ӉR�ӉH�Mp0�    Mp0�@ſ�    H��E�mj ؖ9    ؕK�ؖ9Ө�O    Ө�Oӧ�~�e�6    �e�6@�v     JQ�D��G{أiq    ءUaأiqӷ�    ӷ�ӵ�f̿+�    ̿+�@�,�    I�d~��g�غ:x    ض�/غ:x�ю�    �ю�����J���    J���@��     H��ϻ�!���4�    �Ϯ���4����I    ���I�����    ���@ș�    �M�4��)���.�    �����.��B�    �B��%���[�    ��[�@�P     ɲX~�Ւ��	��    �M��	����b    ��b� ��,��    �,��@��    I��������    � �����.�    �.��(�R�W?:    �W?:@ʽ     J�gT����([�    �"��([��=sO    �=sO�7RS���    ���@�s�    JإB����1Y�    �+�1Y��G�;    �G�;�@r���3�    ��3�@�*     �#-Լ�O.�    �G�'�O.��i"�    �i"��`��Ήa    Ήa@���    JcÄ�+;��_�R    �WZ��_�R�||    �||�rU[Ώ�Y    Ώ�Y@͗     ��F��B#�}�D    �t!��}�DԎ��    Ԏ��ԉ[���6.    ��6.@�M�    J��R��ى��    لi�ى��ԛ    ԛԕ x��F    ��F@�     H��N�d�ٕg0    ُpٕg0Ԩ�    Ԩ�ԡh:�
,o    �
,o@Ϻ�    ��$	�z�٤qB    ٝ�L٤qBԹ
�    Թ
�Ա|����    ���@�8�    I�N�����ٯ�    ٨��ٯ����    ���Խ�o�'��    �'��@Г�    �+U���H�ٽq�    ٵv+ٽq���-    ��-��1��A�2    �A�2@��     I࡫��uM�żm    ٽ::�żm�ށ�    �ށ������O�7    �O�7@�J@    �-V��)-��    ��,,����A�    ��A���?��g�D    �g�D@ѥ�    ʃQ������� �    ��ʂ�� ����z    ���z��2��g�    �g�@� �    Ȯ����y��G$    �ۧ8��G$�     � ��+�ρS�    ρS�@�\     Ɇ���E����    ���0�����    ��� EPτ�:    τ�:@ҷ@    �˒���¾��Ȃ    ��fI��Ȃ�i�    �i����ϕ �    ϕ �@��    ɰ$*�è�� wl    ��s� wl��b    ��b�
s�ϙ�[    ϙ�[@�m�    Jf��%���    ��vR���L�    �L���]ϗ�g    ϗ�g@��     HG�Q��	�+y    � T^�+y��W    ��W�g�ϟ+�    ϟ+�@�$@    Hv���-K��.    �����.�
U    �
U�OϐV�    ϐV�@��    �uN����0�i�    �Qq�i�� A1    � A1�e5ϩ��    ϩ��@���    J1g��<���    �	�E���"    �"�"�ϩE�    ϩE�@�6     ɣ����Q���(    �����(�&��    �&���p���2    ��2@Ց@    J�̫��#���    ������&�    �&��P ϭđ    ϭđ@��    �.�}��mE�s`    ���s`�*ls    �*ls�#���y    ��y@�G�    I�k.��>���    �������,ޣ    �,ޣ�%]�����    ����@֣     ������iX    ����iX�0�    �0��(k���_|    ��_|@��@    ��p@��]���    �	5����3��    �3���,5�ٴ}    �ٴ}@�Y�    ��C��R �#�o    ��+�#�o�8D    �8D�0l7��j    ��j@״�    �Yϧ� A�(x%    �!M[�(x%�=�    �=��5�^���h    ���h@�     ɇࢽf��,�y    �%B��,�y�B<,    �B<,�9�����;    ���;@�k@    ���U�I�0[    �(��0[�Fr�    �Fr��>]��#    ��#@�ƀ    ��_�	���4��    �,���4���K@�    �K@��B�.��I    ��I@�!�    � B��+�9�    �18N�9��P0    �P0�Gk���
    ��
@�}     �vL-��P�>�    �6#k�>��U�q    �U�q�L���~�    �~�@��@    ʞ���k�C��    �;��C���\    �\�R���/�    �/�@�3�    ʛr��b��I?i    �@��I?i�bu~    �bu~�YK�*B    �*B@ڎ�    �7�����M�*    �E��M�*�g[�    �g[��]ǜ��4    ��4@��     �`���I�P�Q    �G���P�Q�jȨ    �jȨ�a���!    ��!@�E@    �o��"i�T��    �K�%�T���oC�    �oC��eW_�s    �s@۠�    ʋ|ӽ%��Y�|    �P���Y�|�t��    �t���j�*��    ��@���    ʏ)@�)���^H�    �U7��^H��z!�    �z!��o�����    ���@�W     ʓ��-9:�c�    �Y���c����    ����u&��9A    �9A@ܲ@    ʛ�ɽ0Ǒ�g��    �^T��g��Ղ[�    Ղ[��z/� �    � �@��    ʫ}�4tY�lq�    �b���lq�Յm    Յm�bm�"Δ    �"Δ@�h�    J�R�5Q��m��    �d
N�m��Յ�?    Յ�?ՀM���9    ��9@��     �S�z�8���q��    �h9��q��Ո"�    Ո"�Ղ���%�    �%�@�@    ���:���t��    �j���t��Չ�    Չ�Մ#�"�    �"�@�z�    �"�u�=t��x)G    �nFZ�x)GՋ��    Ջ��Ն��)"�    �)"�@���    ��8�@~�{lE    �q{�{lEՍu�    Սu�Շݼ�+�    �+�@�1     ��}�A�p�}�    �s���}�Վ�    Վ�Չ&��/_    �/_@ߌ@    �����C�Rڀ;(    �vy�ڀ;(ՐK�    ՐK�Պ�A�2w�    �2w�@��    � �~�F!�ځ�5    �y/eځ�5Ց�y    Ց�yՌ3l�2u�    �2u�@�!`    �l(4�H�UڃV�    �|�TڃV�Փ��    Փ��Վ%Q�7�9    �7�9@�O     J�Q8�HU�ڃ g    �{�ڃ gՓi�    Փi�Ս·�-]    �-]@�|�    �<6�J�ڄ�w    �~��ڄ�wՕ"�    Օ"�Տx��7�?    �7�?@�@    I�ᒽK^�ڄ�7    ��6ڄ�7Օ�    Օ�Տ�}�7��    �7��@���    I�yi�L?�څ{@    ڀp�څ{@Ֆ4    Ֆ4Ր���6��    �6��@��    �3��M޴چ��    ځumچ��՗\�    ՗\�Ց�5�9    �9@�3     ��YܽO�Vڇ�5    ڂ��ڇ�5՘�i    ՘�iՓ&��<��    �<��@�`�    �1�A�QKlڈ��    ڃ��ڈ��ՙӑ    ՙӑՔ��>a    �>a@�`    Hef{�Rg�ډi    ڄOjډi՚��    ՚��Ք��=�    �=�@�     HR�½S�}ڊ"X    څ�ڊ"X՛pZ    ՛pZՕ���?    �?@��    ��A��U��ڋ~�    چ^�ڋ~�՜��    ՜��՗3��A�j    �A�j@�@    �ۛ�W�ڌm�    ڇF�ڌm�՞,    ՞,՘8��E��    �E��@�D�    ��%��Z�Vڎ�8    ډ��ڎ�8ՠ��    ՠ��՚��I`�    �I`�@�r�    �%�\�ڐ5    ڊ�ڐ5բ)�    բ)�՜Y��Juv    �Juv@�     �)��aWGڒ�    ڍ��ڒ�եN�    եN�՟t]�O.�    �O.�@���    �-��c��ڔN�    ڏ_ڔN�զ�    զ�ա ��Mӻ    �Mӻ@��`    ʭ�ǽfs�ږ+'    ڐ��ږ+'ը�    ը�գg�P!�    �P!�@�)     ��~��h=�ڗV�    ڒ
�ڗV�ժL-    ժL-դVH�Q�[    �Q�[@�V�    ʴ�ؽk�ڙ�    ڔ,�ڙ�լ��    լ��զ���V�    �V�@�@    