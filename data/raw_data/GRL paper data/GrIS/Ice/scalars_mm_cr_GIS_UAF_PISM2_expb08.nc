CDF   V   
      time             nco_openmp_thread_number            Description       PISMIP6-Greenland recalculated scalar output. Heiko Goelzer 2019, h.goelzer@uu.nl   history      �Wed May 13 12:17:19 2020: ncks -A -v oarea,rhof,rhoi,rhow,dx,dy /home/hgoelzer/Projects/ISMIP6/Archive_sc/Data/SC_GIC1_OBS0//UAF/PISM2/expb03_05/scalars_mm_GIS_UAF_PISM2_expb03.nc anc_cr_tmp.nc
Wed May 13 12:17:19 2020: ncap2 -O -s *var_tmp=smb(0); smb=float(smb-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 12:17:19 2020: ncap2 -O -s *var_tmp=sle(0); sle=float(sle-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 12:17:19 2020: ncap2 -O -s *var_tmp=limgr(0); limgr=float(limgr-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 12:17:18 2020: ncap2 -O -s *var_tmp=limfl(0); limfl=float(limfl-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 12:17:18 2020: ncap2 -O -s *var_tmp=limaf(0); limaf=float(limaf-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 12:17:18 2020: ncap2 -O -s *var_tmp=lim(0); lim=float(lim-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 12:17:18 2020: ncap2 -O -s *var_tmp=ivolgr(0); ivolgr=float(ivolgr-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 12:17:18 2020: ncap2 -O -s *var_tmp=ivolfl(0); ivolfl=float(ivolfl-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 12:17:18 2020: ncap2 -O -s *var_tmp=ivol(0); ivol=float(ivol-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 12:17:18 2020: ncap2 -O -s *var_tmp=ivaf(0); ivaf=float(ivaf-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 12:17:18 2020: ncap2 -O -s *var_tmp=iareagr(0); iareagr=float(iareagr-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 12:17:18 2020: ncap2 -O -s *var_tmp=iareafl(0); iareafl=float(iareafl-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 12:17:18 2020: ncap2 -O -s *var_tmp=iarea(0); iarea=float(iarea-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 12:17:18 2020: ncdiff -O /home/hgoelzer/Projects/ISMIP6/Archive_sc/Data/SC_GIC1_OBS0//UAF/PISM2/expb03_05/scalars_mm_GIS_UAF_PISM2_expb03.nc /home/hgoelzer/Projects/ISMIP6/Archive_sc/Data/SC_GIC1_OBS0//UAF/PISM2/ctrl_proj_05/scalars_mm_GIS_UAF_PISM2_ctrl_proj.nc anc_cr_tmp.nc      NCO       "4.6.0"    history_of_appended_files         �Wed May 13 12:17:19 2020: Appended file /home/hgoelzer/Projects/ISMIP6/Archive_sc/Data/SC_GIC1_OBS0//UAF/PISM2/expb03_05/scalars_mm_GIS_UAF_PISM2_expb03.nc had no "history" attribute
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
diagnostic     units         m2          |   dx               axis      x      standard_name         projection_x_coordinate    units         m           $   dy               axis      y      standard_name         projection_y_coordinate    units         m           (   oarea                       ,   rhof                    4   rhoi                    <   rhow                    D   time                standard_name         time   	long_name         time   bounds        	time_bnds      units         days since 2008-1-1 00:00:00   calendar      standard   axis      T           �E�@ E�@ B����� @�@     @�p     @�                                                         @�     I��%���m֧F��mg&֮~�֩!�Ѽ;�΅�^ѾQ���Z�;
��p����@���    J!E۹�������U�̉r��A����P&�w��8��)M�,L�>N��@��     ʀW������~U8����@����!��jPP+��Ư��x(M��eLԮM�O�@�z�    �h ��S�׫�CU 3�ף��ק�����$PC.ҽҸqm͚�L<��̓@��    J���ΰD��@U����4�Y���'P������A���L�<F�i�J@Ȝ�    �[����t���U�k�����x�~�QL1���6���pL�������@�.     I�^��7@uV��1�|�.��N5gQ~#�Dͅ�H�Γ�L���΄H8@Ͽ     H��<����=�dV��;h�4���UP�Q���KV��R����QL�Ox��BY@Ѩ     ʿj�� 0L�K��U�H��Iw�DG�e2�QQl�\���b�%�˜L�����,@�p�    IK?�P;�؄�U�ˉ؂�؁�ӕt�Q:�ӑJ�ӓYz�D��L��v�@�@�9@    Ȭw߻U�J؇8xU�yu؆uz؃��Ә)
Q�Ӕ �ӗM��R��L�]��M8�@��    ʉ�Ȼ_�،��Uݕ،H�؉-VӞBP�WHӚ\�ӝێ�`�M ��X�@��@    JV���g�ؠ֣U��8ء~&؝��Ӵ��P׼�ӱ��ӵ�Fπ�Mη�w�=@ڒ�    ʐy�xK&ؚ:�U7*�؜"�ؘ�1ӭ��PN.ӫ�vӯ�7�qK�L���jCx@�[�    ��u6���ز�~T��6ش�7ر�����P�8��Ғ�ˠ�ωɃL��>φ&N@�$     �B����7��*7UzSy�����5����P������A����Ϡp�L��5Ϝ��@��    ��q��VM��U�p{������E��P��u���� ϸ��M&�ϴZv@�ڀ    �EJ��Ǚn���V@�����p�$Q��ǿ�=K��_M��Ǟ�@��    �6�����b���V����p�v]��DQ r��y�����څMX�<���@�     ʐL� 3&�"��V��!;�� ��6��Q0c�4R�5n��	OKM`���@�@    ��o�#��,cuV$���+8U�)��A�Q9`��?��@�k�<�Mr�]�p�@�k�    ʩ�����A_�V���@[��?(��Y��Q���Wc�Xt��G�MY�9��[@�O�    ʑ �"���M�SV�f�L���KS��gK3Q���d�?�fP��<dM4d��j�@�4     ʅ�<�*��W��V<���V��T�B�r�FQTH��o�"�qۓ�%��MBK��"�w@�`    ʞ��2�:�a�VHZ��`�Y�^���~�Qas��z��|��-e0M2��*��@���    �)iv�<�r�n]~Vq�R�m#@�j�aԆ�Q��ԃ��ԅl+�=ZCMJ�,�:0B@��     �/qݼNrpقb4Vtف�Sـz.Ԓ��Q�JQԐ�}Ԓ��I7RMI!/�F�@��@    �
���S�Jم�yV�3مYك��ԖsOQ�"�Ԕ�ԕ�?�KL�MasF�G��@ꩀ    ���b��ُg-V�нَ�Yٍ'�ԡ^)Q���Ԟ��Ԡlk�W�Mu���Te@��    Ɍļtȶٚ��V�Zٙ��٘�dԮ\Q��ԫ��ԭ6x�f�M��/�b	�@�r     �&���w�Iٝ6ZV��"ٛ�ٚʒ԰�4Q�[LԮ.�ԯv*�j��M� ��ex�@�V`    �,�"��
�٨��V��:٧R�٦kԽ�$Q���ԻDԼH��x �M�N%�r�V@�:�    �a���eٴRV�*�ٲ�xٲt���Q��X��N(��"�ЁB�M�9�}+�@��    �廽�����À�V��3��u��� ����xQ����RZ�ٲ7Ј��M���Ѕ�
@��    �����i�˶�V��z��V������</Q�����ED�⏃Ќ��M��uЉp�@�s�    ��🼦3��ӫV�k��X���:��]Qӭ3��R��5�А��M�ޛЍA\@���    �9���!���~�V� ��|5��^u���Q�%���y{���ГqiM��Џ�@�X     ��m�������V˻s���!��ә���Q�A5��]���u�Ж��M�,�В�@��     �2�D��{���QV����ޝ��޸z��K�Q�#;���3����Й�N'�Д��@�<@    �'�1��ms��#V�X���w������CQ�rL�_��:О��Nu�КD1@�`    �����7���C�V������S���{�>�Q�I��
P*�
#�У�kN��П�n@� �    �3�ü�:��?V�!�����������'R ["�����aЧ��NآУe�@�    ˞�{��*���.V�m�k(������R{u����!�Ь�Nq�ЧQ@��    �A����#��[W,��v
����$FR[��!���!n�г+N �RЮ	@�v�    ː�7����)iW�������+9JR)�(Ԧ�(�й��N*��дH#@��    �= 6��i��!DRW������5x4Rpp�2�r�2�y��=�N$ �л�@�[@    �I_���'��W#��$���%,H�<�:R(��9�o�9����5�N)q����A@��`    ˛\����-�TW$]�+�+d��C�7R-s��@�h�@m(�ɺmN(����ux@�?�    ˔Z�����7Z�W"7,�4|�4���NSR6�{�Kx��K3��#PN+]���@���    �<۽�-�@��W(�i�=��>0�X�'R>��U���Ul��٧N2�n��q@�#�    �{yŽo3�F��W-��C|a�D	��_�BRB�?�\�}�[����P;N?p���T�@���    ˚�p�!���N�W1�2�K:��K��h�!RH*��eou�d����pjNI����#�@�    ˆ���)X�XpRW9C'�T�T�U�F�s��RPx��pK��o����azNZ����@�z8    �w[½/���`uKWE��\���]`��|��R]˷�y��x�����lNr�S����@��`    ˯�Ƚ5���h<WW˻�d���d��Ղ��Rr�`Հ�NՀ���<7N~�$��D�@�^�    ˯�>S�sU�Wf�7�o]��o�Ո��R�ϼՆ�Ն����N��*���
@�Р    ˵�F���~i:Wyn�z2��z��Տ$#R�V�Ռ��Ռ�9���N�m}��p�@�B�    ˲��O��ڄ��W�I�ڂ�rڂ��Օq�R�:Փ�Ւ����fN����"a@���    ��V½XD2ڊC�W�\�ڇ�ڈF՛��R�Hՙ�ՙ��	b)N��a�46@�'     ��]�c˦ڑ��W��ڏ?ڏB%գʵR���ա4}ա1���N�]+���@��     ˭��n�=ژ�W��Tږrږ]ի�R�I�ը��ը��~�N�H���p@�H    ��8��v�ڝ��W��sڛ=�ڛ4�ձ�vR� �ծ�tծ����~N��D�ּ@�}p    ���t���uڤ~�W��Xڡ�ڡ̀չR�'�նqն:�0�N����	�@��    ˵�����ګ,{W��ڨo�ڨ`���Rɋ�սw�ս�I��mN�/����@�a�    ��琽�,�ڰ~�W�E�ڭ�kڭ���ƛR�{��}(�Ì��<rNȹ,���@���    ��𴽐;�ڸ2�W��<ڵe�ڵW>��F"R��������{�#h�N����@�F     �🻽�@�ڿ��W��ڼ��ڼ�g���RҋI�ԥ��Ԥ=�&��N�ة� ?@��     �	c��ހ��#W�?��\��'���R��E�ܢ6�ܗ1�)��N�=��"��@�*@    �	m���M ��)W�	���F��4����RԸ3�����届�,�bN�i^�%�@��h    �1�罨�D��O�W��K��Ck��T���IRֵ����1�����/�N���(��A H    ��ea��#^���W��S���:�����2-R�+���������4E
N��,�$A @X    �#�����#��HW��U��
���0��@�Rޔ�����n(�7�N�4��0.�A yh    ��������Wɦk��\���<��dR��g�����B�;�5N�Za�4SbA �|    �R���u����jW�eq��W)�������R�@�������A�2N����9ǄA �    �$���\��+)W�4�e�������R������s�F^uOJI�>)�A$�    �#d����		�W�-v�8�Qn�4�R� �E �(��J�OgV�BbGA]�    �^@��}���Wݤ������n�IcR�h��V��-p�N��O���E�'A��    �#�ͽ���.�W�(��=�to�&�R��{�$�J�$��S�WOd��KA��    �Q2��D��W��	����=8�,"�R��f�*/��)��WcO˵�N6KA�    �b�[��^����W�����4����1cVR���/mw�/
��[~#O���RsDAA�    �U_����$n�W���"Ba�"���9:R��r�7��6��aX OG��XS�A{    �2�S���*��W�A��(v��(��@�R�y��>�=���f�O?Z�\J�A�     �[���
��/��W���-�h�.��E��SHq�C���CY��iѧO l��_��A�0    �/7�'�6�UW� ��4
�4�S�M`�SX��KK2�J���n��O%N��d��A&@    �4���(J�;�GW���9{�9���S1CS,�Q:�PB��svO+���hE�AB�    