CDF   V   
      time             nco_openmp_thread_number            Description       PISMIP6-Greenland recalculated scalar output. Heiko Goelzer 2019, h.goelzer@uu.nl   history      �Wed May 13 12:08:00 2020: ncks -A -v oarea,rhof,rhoi,rhow,dx,dy /home/hgoelzer/Projects/ISMIP6/Archive_sc/Data/SC_GIC1_OBS0//IMAU/IMAUICE2/expb05_05/scalars_mm_GIS_IMAU_IMAUICE2_expb05.nc anc_cr_tmp.nc
Wed May 13 12:08:00 2020: ncap2 -O -s *var_tmp=smb(0); smb=float(smb-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 12:08:00 2020: ncap2 -O -s *var_tmp=sle(0); sle=float(sle-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 12:08:00 2020: ncap2 -O -s *var_tmp=limgr(0); limgr=float(limgr-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 12:08:00 2020: ncap2 -O -s *var_tmp=limfl(0); limfl=float(limfl-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 12:08:00 2020: ncap2 -O -s *var_tmp=limaf(0); limaf=float(limaf-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 12:08:00 2020: ncap2 -O -s *var_tmp=lim(0); lim=float(lim-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 12:08:00 2020: ncap2 -O -s *var_tmp=ivolgr(0); ivolgr=float(ivolgr-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 12:08:00 2020: ncap2 -O -s *var_tmp=ivolfl(0); ivolfl=float(ivolfl-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 12:08:00 2020: ncap2 -O -s *var_tmp=ivol(0); ivol=float(ivol-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 12:07:59 2020: ncap2 -O -s *var_tmp=ivaf(0); ivaf=float(ivaf-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 12:07:59 2020: ncap2 -O -s *var_tmp=iareagr(0); iareagr=float(iareagr-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 12:07:59 2020: ncap2 -O -s *var_tmp=iareafl(0); iareafl=float(iareafl-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 12:07:59 2020: ncap2 -O -s *var_tmp=iarea(0); iarea=float(iarea-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 12:07:59 2020: ncdiff -O /home/hgoelzer/Projects/ISMIP6/Archive_sc/Data/SC_GIC1_OBS0//IMAU/IMAUICE2/expb05_05/scalars_mm_GIS_IMAU_IMAUICE2_expb05.nc /home/hgoelzer/Projects/ISMIP6/Archive_sc/Data/SC_GIC1_OBS0//IMAU/IMAUICE2/ctrl_proj_05/scalars_mm_GIS_IMAU_IMAUICE2_ctrl_proj.nc anc_cr_tmp.nc      NCO       "4.6.0"    history_of_appended_files         �Wed May 13 12:08:00 2020: Appended file /home/hgoelzer/Projects/ISMIP6/Archive_sc/Data/SC_GIC1_OBS0//IMAU/IMAUICE2/expb05_05/scalars_mm_GIS_IMAU_IMAUICE2_expb05.nc had no "history" attribute
          smb                 
_FillValue        |�     	long_name         surface mass balance   missing_value         |�     units         kg s-1          �   sle                 	long_name         sealevel equivalent ice mass   units         m           �   limgr                   	long_name         grounded ice mass      units         kg          �   limfl                   	long_name         floating ice mass      units         kg          �   limaf                   	long_name         ice mass above flotation   units         kg          �   lim                 	long_name         ice mass   units         kg          �   ivolgr                  	long_name         grounded ice volume    units         m3          �   ivolfl                  	long_name         floating ice volume    units         m3          �   ivol                	long_name         
ice volume     units         m3          �   ivaf                	long_name         ice volume above flotation     units         m3          �   iareagr                 	long_name         grounded ice sheet area    units         m2          �   iareafl                 	long_name         floating ice sheet area    units         m2          �   iarea                   	long_name         ice sheet area     units         m2          �   dx               axis      x      standard_name         projection_x_coordinate    units         m           d   dy               axis      y      standard_name         projection_y_coordinate    units         m           h   oarea                       l   rhof                    t   rhoi                    |   rhow                    �   time                standard_name         time   units         days since 1900-1-1 00:00:00   calendar      standard   axis      T           �E�@ E�@ B����� @�@     @�p     @�                                                         @�     I������"��    � �3�"���7%�    �7%��4��J�<�    J�<�@���    ���>0�qVd    �o��qVd҇�    ҇�҆�_M���    M���@�`    I�V|���	���    ��Ԅ������    �����~�M��7    M��7@�9     I��[��Z�iP    �d�iP�߸    �߸���M�\I    M�\I@�f�    J�+����?    ���?�.��    �.���&:�NS�    NS�@�`    �>b����0B�    �(���0B��FWL    �FWL�=��N�2    N�2@��     ɢ���Aj��{y    �sA%�{yӍ;�    Ӎ;�ӈ�2���    ���@��    ʧ@����Sث�E    إ��ث�E��W�    ��W�ӺB^�Ǉw    �Ǉw@�@    ʦJ黥J���R6    �����R6��+�    ��+���������    ����@�K     I���������j    ��:���j���D    ���D���OL��w    L��w@�x�    ʣ<���l�		�    ��C�		��4�    �4����b�k    �b�k@�@    G?"0�� ��ư    ���ư�'i�    �'i��"��΃��    ΃��@���    ʘ����o�'W�    �#%g�'W��<Ni    �<Ni�7��΀�r    ΀�r@��    J�B�w�3�    �+���3��Jj�    �Jj��A!/�m+1    �m+1@�/@    �dzE�a��EmQ    �=!��EmQ�^(�    �^(��T�Ό��    Ό��@�\�    �^u�&n��]��    �QQ��]���y�F    �y�F�k�xιz�    ιz�@犀    ʒ�R�6�`�r1�    �e���r1�ԈDt    ԈDtԁ4L��-�    ��-�@�@    �
�z�>���|�    �o�X�|�Ԏx    Ԏxԇ�Ω�+    Ω�+@���    �`d"�H��ل�    �|t�ل�ԕ+[    ԕ+[Ԏ
�Ζ!�    Ζ!�@��    �3;̼S��ًt�    م�ًt�Ԝ�    Ԝ�ԕ�9�O�w    �O�w@�A     ��H�g�ٗ�V    ّRxٗ�VԪ�l    Ԫ�lԣ�����    ���@�n�    HQ�ѼlN�ٚ��    ٔ��ٚ��Ԯg�    Ԯg�ԧ7&΀�z    ΀�z@蜀    �}�)�vh�١Yy    ٚ�f١YyԵ�    Ե�Ԯ\�ν    ν@��     ��`޼�F٩�    ٢N#٩�Կ     Կ Զ�Rγ��    γ��@���    ��3���
�ٵ    ٭��ٵ��Α    ��Α��\���y�    ��y�@�%�    ���N��*�ٿZZ    ٷ�ٿZZ��S    ��S�������    ���@�S     �󶼝���QH    ��v���QH��	�    ��	���34�� �    �� �@��    ��x����p��`M    �р���`M����    �����뿩�)!    �)!@�`    ʤwϼ������    �ڨS������    ��������    ��@��     �z��c0��Ą    ���c��Ą��    ����J$��    ��@�	�    ��Ҽ�xc���y    ������y�	ё    �	ё�]D�&�    �&�@�7`    ��[ʼ�x���5B    ��S��5B���    �����E���    ���@�e     �c������    ��O���gc    �gc�eV�x�    �x�@��    �%2{�ӝ��	��    �[�	����Q    ��Q���,�    �,�@��`    �5×��,~�Ct    ���Ct�"V    �"V�6��<ӳ    �<ӳ@��     ������T�    ���T��&�    �&��!�
�8Մ    �8Մ@��    �ˏ4��
���^    ����^�,��    �,���'��I�R    �I�R@�I`    �6����E
    ��.�E
�38�    �38��-���Q��    �Q��@�w     �d��� X�&�    �!jH�&��:�h    �:�h�5���TJ#    �TJ#@뤠    �#A ��-�/&�    �*n5�/&��E�    �E��?���[�    �[�@��@    �R��~�6��    �1��6���M�F    �M�F�H>��c��    �c��@�      ������;ɟ    �5��;ɟ�SP    �SP�L���s��    �s��@�-�    �]������F�    �@+�F��^�q    �^�q�Xsσ��    σ��@�[@    ʸΊ� #��OĜ    �IgL�OĜ�i��    �i���b�_ώ{�    ώ{�@��    ��?L�$G��U��    �N���U���p�x    �p�x�h~�ϝ�V    ϝ�V@춠    �pI��(���[;�    �Tp�[;��v��    �v���n��ϡ�#    ϡ�#@��@    ˉ�w�0N��el�    �]���el�ՁK    ՁK�y�ϭ     ϭ @��    �[`p�8���o��    �h��o��Ն��    Ն��Ղ��ϲ.    ϲ.@�?�    �FKd�?{��x�b    �p���x�bՋ��    Ջ��Շϵ?�    ϵ?�@�m@    ˆ�2�F�ڀ{N    �yIڀ{NՐ��    Ր��Ռ�ϵ܆    ϵ܆@��    ���N8څ�M    ځ�Vڅ�MՖT�    ՖT�Ց�~ϻ��    ϻ��@�Ȁ    ˕E��S;�ڈ��    ڄ��ڈ��ՙ��    ՙ��Օx���{�    ��{�@��     ˲�}�\tڎg�    ڊY�ڎg�ՠ>�    ՠ>�՛����{�    ��{�@�#�    ˃\�f9eڕ�    ڐ�ڕ�է�    է�բ����κ    ��κ@�Q�    ��ɽn7Nښ(�    ڕ̓ښ(�խx|    խx|ը������    ����@�     �H��s��ڝ�$    ڙ,Eڝ�$ձ|�    ձ|�լ\���    ��@��    ˢ�V�z*�ڡ�)    ڝPhڡ�)նC�    նC�ձ��٪�    �٪�@�ڀ    ˯������ڨ0�    ڣlhڨ0�սB�    սB�շ�s��    ��@�     ˂a����ڮ�    ک�ڮ����2    ���2տ(���N�    ��N�@�5�    ˭GG��;�ڴ=!    گ�ڴ=!���r    ���r�����4�    ��4�@�c`    �j�ҽ�#Lں�'    ڵGOں�'����    ���������e�    �e�@�     ˆ	����ڿ#B    ڹ�+ڿ#B��    ������F    ��F@��    ˔落��/��Bv    ھ���Bv��ؒ    ��ؒ�����	�e    �	�e@��`    ˗K۽��ɼ�    ��O��ɼ����    ������H��    ��@�     �׬������Ϝ4    ����Ϝ4��T    ��T��nN�|�    �|�@�#�    ���콦�D�א    ���1�א��9    ��9��*���W    ��W@�:�    �ڰ[������V    ��3-���V���N    ���N��h���    ��@�Q�    ��/S������G    ��"���G��7    ��7��V�"SQ    �"SQ@�hP    ��	��H����    ��H�����R    �R����-?|    �-?|@�0    ˲�L���*��!�    ��D��!��+�    �+�����1�k    �1�k@�     ���ԽƼ6� ��    ���� ����    ������8��    �8��@��    ��OW������    �n������    ������<|�    �<|�@�à    ����Y��	a�    ����	a����    ����C�B�    �B�@�ڀ    �"��a����    �
������ ��    � ������K�e    �K�e@��P    ������.�U    �<��U�%�    �%��!.��Q�    �Q�@�     �������A��^    �T���^�+�	    �+�	�&�~�a��    �a��@��    �%����(=    ��F�(=�0�R    �0�R�+�*�i�-    �i�-@�5�    ����;\�"��    ����"���6��    �6���1�~�qmz    �qmz@�L�    ��� ũ�&��    �!��&���;lg    �;lg�6=��w�    �w�@�cp    �1�D����+y�    �&�G�+y��@��    �@���;��Ё?D    Ё?D@�z@    �B�h�	��1�    �,qi�1��GG'    �GG'�B�Ѕ~�    Ѕ~�@�     �����7T�    �2�~�7T��NLD    �NLD�H��Ћ��    Ћ��@��    �Q�Ͼ��;�m    �7#��;�m�S|�    �S|��N�А"     А" @��    ������B�<    �=���B�<�Z��    �Z���UsSГ�    Г�@�Ր    �$X����GE�    �Bd��GE��`<>    �`<>�Z��Иf    Иf@��`    