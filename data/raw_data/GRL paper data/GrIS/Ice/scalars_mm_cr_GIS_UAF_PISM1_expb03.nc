CDF   V   
      time             nco_openmp_thread_number            Description       PISMIP6-Greenland recalculated scalar output. Heiko Goelzer 2019, h.goelzer@uu.nl   history      �Wed May 13 12:15:58 2020: ncks -A -v oarea,rhof,rhoi,rhow,dx,dy /home/hgoelzer/Projects/ISMIP6/Archive_sc/Data/SC_GIC1_OBS0//UAF/PISM1/expb03_05/scalars_mm_GIS_UAF_PISM1_expb03.nc anc_cr_tmp.nc
Wed May 13 12:15:58 2020: ncap2 -O -s *var_tmp=smb(0); smb=float(smb-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 12:15:58 2020: ncap2 -O -s *var_tmp=sle(0); sle=float(sle-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 12:15:58 2020: ncap2 -O -s *var_tmp=limgr(0); limgr=float(limgr-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 12:15:58 2020: ncap2 -O -s *var_tmp=limfl(0); limfl=float(limfl-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 12:15:58 2020: ncap2 -O -s *var_tmp=limaf(0); limaf=float(limaf-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 12:15:58 2020: ncap2 -O -s *var_tmp=lim(0); lim=float(lim-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 12:15:58 2020: ncap2 -O -s *var_tmp=ivolgr(0); ivolgr=float(ivolgr-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 12:15:58 2020: ncap2 -O -s *var_tmp=ivolfl(0); ivolfl=float(ivolfl-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 12:15:58 2020: ncap2 -O -s *var_tmp=ivol(0); ivol=float(ivol-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 12:15:58 2020: ncap2 -O -s *var_tmp=ivaf(0); ivaf=float(ivaf-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 12:15:58 2020: ncap2 -O -s *var_tmp=iareagr(0); iareagr=float(iareagr-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 12:15:58 2020: ncap2 -O -s *var_tmp=iareafl(0); iareafl=float(iareafl-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 12:15:58 2020: ncap2 -O -s *var_tmp=iarea(0); iarea=float(iarea-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 12:15:58 2020: ncdiff -O /home/hgoelzer/Projects/ISMIP6/Archive_sc/Data/SC_GIC1_OBS0//UAF/PISM1/expb03_05/scalars_mm_GIS_UAF_PISM1_expb03.nc /home/hgoelzer/Projects/ISMIP6/Archive_sc/Data/SC_GIC1_OBS0//UAF/PISM1/ctrl_proj_05/scalars_mm_GIS_UAF_PISM1_ctrl_proj.nc anc_cr_tmp.nc      NCO       "4.6.0"    history_of_appended_files         �Wed May 13 12:15:58 2020: Appended file /home/hgoelzer/Projects/ISMIP6/Archive_sc/Data/SC_GIC1_OBS0//UAF/PISM1/expb03_05/scalars_mm_GIS_UAF_PISM1_expb03.nc had no "history" attribute
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
diagnostic     units         m2          |   dx               axis      x      standard_name         projection_x_coordinate    units         m           $   dy               axis      y      standard_name         projection_y_coordinate    units         m           (   oarea                       ,   rhof                    4   rhoi                    <   rhow                    D   time                standard_name         time   	long_name         time   bounds        	time_bnds      units         days since 2008-1-1 00:00:00   calendar      standard   axis      T           �E�@ E�@ B����� @�@     @�p     @�                                                         @�     I��P��ϫ��J�S�F6��q���fb��#�N������٭��#*�K�� ���@���    J�o��<՚�4T����;@��i��ЮE�O��qЃ�c�R���T��K��6d@��     ʁآ� q��Q8+T!���I� �N���km�O5�s�h���cu�f�L�f���@�z�    �hkU��T׾SVT6hX׹J�׼���+$OMB7�Ԑ��Ѐ��8�L,� �-J�@��    J���ۧ׹��TJ;#׳�<׸���ROc���� 1��-G�M�LS�,�?��@Ȝ�    �_R��{��44S|���\'����DON�W���#���Ό�xLh��΅R�@�.     I"������;S����t����$8�N�Fq�#�c�,ΤQ+L�U!Κ��@Ͽ     H�6C��]
�-�Tsl,�	7�:*�1�hO��h�0�~�,5!ο��L�E�ε_b@Ѩ     ʾ�
�)hh�[��T�V
�UW�ZQ6�w�O�/��u���o�>��؇L�"����W@�p�    IY�/ؕ�d�T}��](6�c�ӀI�O��N�u��x����mL�X����L@�9@    ��(��@x�|�ӭH��q���|ifӍ�j���7ӎ*Ӈ�)�K�L3KD�~�@��    ʉ���h��ؙR�T�;�ؒQQؘ��Ӭ�O�qӫ��Ӥ���&�L��f�"[�@��@    J
q�h%�ؙvj��J1ؑ��ؙ��Ӭ���WӬ�ӤE��.�cKk�-�[@ڒ�    ʏaa���Pصf�ԙ%
حP�ص���� XϬTq��̭����G���7�J-�@�[�    ��W���u����ԝj��ҿ
��e:��P>ϱ#+��a��%��\L�́��`\@�$     �7r������sRr�����M����G�M��$�Cp� �w�gV��g4��j�@��    ��ԏ��f� �U%A�������kP9���Tv�	X>πIr�!5�ρ��@�ڀ    �C�ջ�t��
|�U�������	c$��P�r���2�6�υ�N��φ��@��    �-W� {
�*�pS���!�8�*Ù�@K�OM��@(�5�]Ϡ��]�ϧ��@�     ʎ���n��;@IՅ�`�0�s�<K��R�}Ж�5�S��F��Ϭ@���jϸ��@�@    �0G���Q���]�y�F���R�l�k�L�y{��l���_y�Ϸ�G͵Q��+�@�k�    ʣH˼*�?�bw�չ��VoJ�c���~֛���QԀ<�qLH��V��گ0���@�O�    ʌ\��6��qo^���d���sm�ԇ�"��XԈ�5Ԁ���`��� ��ݰ�@�4     ʂ��A��ـ�7��$�sj�ف��Ԑ�i��wԑ�Ԉ��ܾ*�������@�`    ʕ[�M�3وk���`ف;�ىg5ԙ���i�Ԛ��ԑlu�������+P@���    �"෼bUٖ[��M�َnٗ9[ԩ1��&�Ԫ+)ԠE���B������8@��     �'�?�k=�ٜl����"ٓ��ٝ=�԰K��,�԰�wԦu��j/����	`�@��@    �sc�|��٨B��i�ٟG٨�Խ+���d�ԾԳ �	����R�}'@ꩀ    ����w ٵ&�՚�!٫��ٵ����Э��̅���!	�g͹�j�6�@��    �{{2��R�ٹ�Պ��ٯ9ٹ�O��DMЛ�����G��,��#�ͤ@��E�@�r     �������:~բt�ټ�������/�ж�~�����E��!�Ͱ�S�&��@�V`    �%oD������^�Ս�H���������П����`��PT�)%0ͥ�W�.R�@�:�    �W58��]@����պu���K"��}l�e����h�κ�����45|ͱ_c�9�w@��    ������������T��i���x��
�}�	��#��;�%ͻS��A��@��    ������x���k$��x�����j���-����$�����Cջ͹e��I��@�s�    �ԩ�������M���M`���/t�a�����S�Lm���Z�R�v@���    ��$��>:�g�����������]��x^��r��Z�P�Ͷ���V>�@�X     ���߼ψ��
c������:�
�~����i��XS�ڏ�W[��1��]3�@��     �*��ڼ������ts�	���L��$&���:�$����
�`#�ͯS5�e�8@�<@    ��(��3`�����e{�!C�J�,I���f�,~*�"/��h�iͱa{�n�u@�`    �Om��
� o�I]���� �e�4�7�b���4���)���s/�͞��x&�@� �    �*���v�(|�����Bc�(�E�=���zp�=���2��|e0ͅ�ЀJ.@�    ˖ʽ���4�U8���)���4���KY�PP%�K%��?*Є���`K�І}@��    �1�߽��<3U���0��;�v�SƢP��q�Se;�GeЈ�p���Њ/'@�v�    ˉ���|�F�U��;"��Fp��_�hQ���_L��R�0Ўw���Џ�R@��    �/�=�ek�NO�V��B.�M���h(mQ���g���Z��В�Z̰�Гi@�[@    �=�� ��V��U�`3�JE�V<��q�Q
���qv�cf$З+̪�<З��@��`    ˒�{�)02�a�0VA�Tȥ�a?��~
VQ���}w��op�Л�l��М0�@�?�    ˋY&�1���l�9U�a�_^��lm�ՅD�P�\�Յ��{Z/С���AС��@���    �.Ⴝ77�tPnU�W��fmV�s��Չu�Qj&Չ/ Ձ��Х�K���Х[�@�#�    �i+?�>�K�~(U�6 �o�y�}��Վ�yPڊ�Վ��Ն��Ъ�?ː<�Ъ�N@���    ː!��G�ڄ�{U���zknڄz�ՕX�Q
��ՕdՌ�<б�L@ZKа��@�    ��N��ډ��U�Vڂoډ�S՛6hQ�՚�Ւd�е��Lj�Eе= @�z8    �f{��V)EڎѼV	[�چ�,ڎ�ՠ��Q��ՠh�՗�*лQ�L��hк�@��`    ˥�_�ڔ��U�x�ڌ��ڔ�Aէ�6P�׆էi�՞9���R�Lć����V@�^�    ˣ���h�Oښ�kU���ڒfDښ��ծ^�P��Pծ"�դ�X��gRM����=�@�Р    ˪�%�rUxڡ*�U�k+ژcyڡ�յ[GP�յ1�իz��ˤ�M(��ʂ`@�B�    ˧���{�ڧ�����ڞn�ڧ��ռ|��m�ռ}�ղG��ѵFL�����,�@���    �ݎ���$�گ���q�ڦ1�گ�0�ŬWχ�[�Ŵ�ջk���L�� �؊�@�'     ��/���ڷj�Ԛx�ڭ�ڷt;��d�ϭ����o���h6��V�L�u4�މd@��     ˡ{�����ڽ�1Ջ!tڳu'ڽ����ElМ�l��l����k��L�t;��-�@�H    ��i���T^������(ں������݄6������������L�����/�@�}p    �зl��7��bP� �������̲������4�L��Wk�����M'L�!���w@��    ˨���\��p�""���� ��g����6r����P�����	L�0���)�@�a�    ��b��������%�/�;��Z���5���i`�E�����,��t�����Lлv����@���    ��Y��2��ry�G���ؐ����H� �m�`��� ����+�yL���� @�F     ��^��m��섍ց;���g������ёlJ�[������+mK�<�W@��     �1���4����ָ-w��cW�����
N���@�
�G�P�	�2��d��
�@�*@    �H���C���1�=��N�����U�����9���L����D@��h    �(j��[�����;��>f�����&����<��|��}�7C�>�A H    ��#Ͻϭ��	#���G��v�	���R�a���h����˜�u�9��0A @X    ��/�����VL���r��a� +�$a�� �z��k�[�͖�&��A yh    �	����
��Q��>�A���*�%k��)��&����0�͕gz�[xA �|    �H�w��It����+�����:��,ˆ�A/��-���%��2�Ͳ,� �(A �    ���A�����>*�����o��2��U�O�3i�*�f�#)��7��$��A$�    ��q����#���R���u��$d��8��l��8���0��&Vv��6�(T�A]�    �S������*e��W	X�#1
�+<��?���q���@���7���*�+����,��A��    ������/ik�Yk�(��0B��Eb��tL��FW;�=.E�-��㪗�/�A��    ��|�	k��47p�U�P�,�h�5R�J��p���K���B{�0����\}�2p�A�    �W4.����;�V�D�3���;���R���q�H�StP�J
�5h���&c�6��AA�    �J��˙�A�{�Op>�9���BV��Y��il��Z�t�Q*�9�ͦ���:e�A{    �(�����F��UJ��?(>�G���_���p�`���W��<)͠�0�=P{A�     �Q]����MdZ�Y��E���N>�gX�u��hZ�^Vm�?�͜�]�A�A�0    �%n(�!'��R���_�P�J�T�Sp��l��|��m���d_�B�s͘S��DA&@    ��)N�%0�W���g���O���X�V�r�n҂gg�s�=�i�V�E��͓��G�A1�    