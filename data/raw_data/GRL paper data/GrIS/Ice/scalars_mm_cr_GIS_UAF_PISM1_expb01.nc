CDF   V   
      time             nco_openmp_thread_number            Description       PISMIP6-Greenland recalculated scalar output. Heiko Goelzer 2019, h.goelzer@uu.nl   history      �Wed May 13 12:15:45 2020: ncks -A -v oarea,rhof,rhoi,rhow,dx,dy /home/hgoelzer/Projects/ISMIP6/Archive_sc/Data/SC_GIC1_OBS0//UAF/PISM1/expb01_05/scalars_mm_GIS_UAF_PISM1_expb01.nc anc_cr_tmp.nc
Wed May 13 12:15:45 2020: ncap2 -O -s *var_tmp=smb(0); smb=float(smb-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 12:15:45 2020: ncap2 -O -s *var_tmp=sle(0); sle=float(sle-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 12:15:45 2020: ncap2 -O -s *var_tmp=limgr(0); limgr=float(limgr-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 12:15:45 2020: ncap2 -O -s *var_tmp=limfl(0); limfl=float(limfl-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 12:15:45 2020: ncap2 -O -s *var_tmp=limaf(0); limaf=float(limaf-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 12:15:45 2020: ncap2 -O -s *var_tmp=lim(0); lim=float(lim-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 12:15:45 2020: ncap2 -O -s *var_tmp=ivolgr(0); ivolgr=float(ivolgr-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 12:15:45 2020: ncap2 -O -s *var_tmp=ivolfl(0); ivolfl=float(ivolfl-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 12:15:45 2020: ncap2 -O -s *var_tmp=ivol(0); ivol=float(ivol-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 12:15:45 2020: ncap2 -O -s *var_tmp=ivaf(0); ivaf=float(ivaf-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 12:15:45 2020: ncap2 -O -s *var_tmp=iareagr(0); iareagr=float(iareagr-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 12:15:44 2020: ncap2 -O -s *var_tmp=iareafl(0); iareafl=float(iareafl-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 12:15:44 2020: ncap2 -O -s *var_tmp=iarea(0); iarea=float(iarea-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 12:15:44 2020: ncdiff -O /home/hgoelzer/Projects/ISMIP6/Archive_sc/Data/SC_GIC1_OBS0//UAF/PISM1/expb01_05/scalars_mm_GIS_UAF_PISM1_expb01.nc /home/hgoelzer/Projects/ISMIP6/Archive_sc/Data/SC_GIC1_OBS0//UAF/PISM1/ctrl_proj_05/scalars_mm_GIS_UAF_PISM1_ctrl_proj.nc anc_cr_tmp.nc      NCO       "4.6.0"    history_of_appended_files         �Wed May 13 12:15:45 2020: Appended file /home/hgoelzer/Projects/ISMIP6/Archive_sc/Data/SC_GIC1_OBS0//UAF/PISM1/expb01_05/scalars_mm_GIS_UAF_PISM1_expb01.nc had no "history" attribute
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
diagnostic     units         m2          |   dx               axis      x      standard_name         projection_x_coordinate    units         m           $   dy               axis      y      standard_name         projection_y_coordinate    units         m           (   oarea                       ,   rhof                    4   rhoi                    <   rhow                    D   time                standard_name         time   	long_name         time   bounds        	time_bnds      units         days since 2008-1-1 00:00:00   calendar      standard   axis      T           �E�@ E�@ B����� @�@     @�p     @�                                                         @�     �I�˺�V�;�+S4`�9��:���S�NJ���RF��QL�&JK5M���@���    JWB�	{x�3���-.T�,�q�6fZ�J4x�B�M�M?��B��̪x����-����@��     JAݺ6G�@���>V�5_-�C{�X��$�j�[s��L���=��r��+�@�z�    �> L��y�ׯ����H ע�k׼|q��M��_:��Aҷ<���;�Oa��"v@��    HuVi������-�����й���b��#2�\���d���k��9͂M��:��@Ȝ�    ��"�ﵷ�"�������)��73S��b*�?.e�)�G�T�o�tX$Έ��@�.     ��,޻���E�-���x�7���L���^����8�f���N��·�#�[��ΣZ�@Ͽ     �4w�7u��u��Ԋ��f���|�[ӊYy��+	ӎ%Ӂ��Θ���KT�α�?@Ѩ     I%�E�؄�]� �c�x��؈��ӕO���ә�Ӌ�fΫ6�da����7@�p�    H����Xamؐĥ��W؈sؕQ�Ӣ�h�#��Өoә3ο�	�pWM����@�9@    ��'��yhoت���K�y؜�Fر ���H�eI��-�Ӱ|�����ڡ�@��    �>׍��]��ƹ��H�+ظ����;�ߞ��a����m��$#���ӎ/�-�@��@    I1w�������g֒���˷���
V���.Ѥ�$�����=8�(��,Mq�S�j@ڒ�    J[���"��r�֤���|�������Ѹ���
�����:O�B���j�z@�[�    ɑ[�����C-֚�7��x�n���Ѯ,!��:7�H���<�A�w�I@�$     �Z������x�֔�{��$�+�$�	ѧ,��*q�m��Wɻ�A
τ@��    I��d���3�]�օC������.ԥѕ���3�S���i��AUeό��@�ڀ    �@H����a�*0��N,D���-iX�?���h L�C"��/.��xF��2"^ϒg�@��    ʪ���ԁ�?w �Rã�/�Z�B��WsW�m*��[(�E�Cω��2��ϠBT@�     Jr̨���Ag��V��1d��D��Y���qe��]h.�G�Ϗ`��/!�ϥE	@�@    ʚM��#�R�A�TaR�B���V��m%��n�l�p���Z��ϖ#��'L�ϫZ@�k�    ��E�"]��\���Gq)�L4f�_ş�xLZ�`mU�{��e�Pϗ���!�|Ϭ28@�O�    �&dX�,\G�i�p�2�|�X���l�&ԃ���IW�ԅ+h�s��ϡ5���ϴ9�@�4     �e�[�4^!�uV�,g�b��w��ԉ��B ԋd�B�ϩ^���ϻy�@�`    ��>ڼF6�ن��4�a�yI�ه��ԗh�K�GԘ�eԌB3Ϸ#T��,��?�@���    �A�	�Q��َ4<�@γك��ُ��Ԡ��X�ԡ��Ԕ}������=���P�@��     ȣpT�Z�ٔ���H��ى~�ٖ77ԧE�aЛԩ�Ԛ���'T�(��J�@��@    ��T�l`7٠!��X��ٔ�V١ӼԴ1v�t�Զ�ԧCU�����v��A@ꩀ    �*-�w��٧҇�^�Sٛ��٩��Լإ�z�%Ծͯԯ?z��
D�p���x]@��    H�R�|��٫V�\�2ٞ�٬�F���i�x����x�Բݴ����������@�r     ɿn����Aٲ�`�j��٥�Gٴ����ф$p��*OԺ����������w@�V`    I������_ٷq�OX�٩��ٸ�"���?�iRA����Կ
���w��8
��f@�:�    ��T���پ���2Zsٱ���^�����H�M��w���F�����@5�&@��    �s༒�������=�ٸ����p����TŊ��3�Ϧ�����-��S�@��    ʏ����0�ѱw�H�X����B����f�a�=�������E���t���@�s�    ʸj����^�����H�?���h��c������b&���_��纰�+��
���1@���    �������,��M�S���9���L�� ��nN��L����r��
e�!#`@�X     ʖ�ܼ�k*����VH�������"�}9�q ��nZ���<� hA�_Q�)>6@��     ��ռ�9��\T�L���F �������f����/��y�$���^��-��@�<@    ʡ"�������1�C���y���C��\_�� ����-�0��5�*@�`    ʛB�ȏ]��J�Xx���=>�����s�C�����Q�4�����=z�@� �    J4����Й�
���Y�� *������t1!�I�8��:�U����C�E@�    ʦ�Y��4d���1���/�ɟ�#E3�G�|�$����DD�:a�Lq�@��    ��n��������X(����M3�+�5�"mT�,����D�M �չ�UMa@�v�    �m��t� g#�ھH�1i� Ԃ�4P��%t�4�b�&��T����kF�\NJ@��    �ʳ?���~�&~�ժ4���&���;Zaп�O�;�$�-[��Zf���>�ah�@�[@    �6�� �d�.o��u�!���.�6�DJ1Љ���D�&�5���a���{��h�m@��`    �J��M��6�Պ�y�(�>�6Q��L�М)�M)�>G�j�������q��@�?�    ����7��=���o���0YG�>,��U�fІ�J�U���Fp��rX(���\�x�+@���    �p��h`�F��Զn��8"�F���_���I��_���O3T�}mV��4Ё�{@�#�    �*�`�-��PqUD��@�[�O�H�j`P]D&�i��XȳЃ�ͮ��ІV�@���    ���7����X	U!���G�5�Wٙ�s{P6B�r���a �Ј�nͤm�ЋU%@�    �N���'D~�c9�@s?�R^>�cE&��=�X�0����l��Џ�q͵��В]�@�z8    �
a�-n(�k|?�73�Zn�k�Մ~+�NՄ���uq�Дxͷ�YЖ�)@��`    ʲ ��2`��rg���u�`Wt�r��Ոc�!��Ոw7�|r)И2�͵��Л
@�^�    �!ڽ9
��{��ԚA��h�I�{�FՍ�Hϭ��Ս�!Ղ�hН�cͧ�/Рx<@�Р    ʧ�C�=�'ڀ�R�/sv�n��ځ �Ց#��En<Ց)�Ն7Сj�͓�tУ�&@�B�    �;
i�E�چ�U:��w�6څ��Ֆ�P��Ֆ�$ՋrVЦH�͌L~Шy�@���    �J��L�	ڋ��rڀ�(ڋ/g՜��0�M՜�Ր�[Ы�|ͧ�Ю\�@�'     ˓�G�V��ڑ�n��Bڇhڑ�գ�:�vդ=՗�Tв%���BKеF�@��     �_��_kڗ47�6	�ڌFڗ�<ժ%`�L��ժ��՝آиI��#л��@�H    �Q���f�mڜQ�o�ڑ/ڜ��կ�"ц�rհmգ_)н����/%��'d@�}p    �o�)�oI,ڡ��֑�Pږx�ڢjZնOѣ�vն�թRy��L��#��@��    ����u�6ڦG�֙�ښ��ڦ��ջ�ѭ*�ջ��խ�@��mu���~��D@�a�    �=��}�Aګm"ֶb>ڟl�ڬ#�������;Z���ճe��̮Q��'���[@���    �3�����گ��ּaAڣr�ڰ�J���#�����Ơշ��ѳ^�/���@�F     ˫�ʽ���ڷ�كoڪn�ڷ��������)���տț��6���g���0@��     ˦P޽�1'ھ����P�ڱ��ڿs���b������o���Ѯ�����!�T���\@�*@    ˻
��8���f��J1ڹ(��k]��A������f���Z��³�/.��;5@��h    ˿���d��΁���W����ϟ���`�� �P��[����6��9N���5A H    ˞潞����w��!���Ǩ��ֺ���5��5�h��v�����-�K�\���A @X    ˜���-a�ܩ5�&Q"��{H������M��;&����.��Y7��3��V�+���qA yh    ˣ�m���	��ԋ�-�n��`���0� /��C�� �������x�^*��d�A �|    ���������,`�9����y/���!��D�Q)���n��7��ch�j˶��A �    ˀN}������Q��?���L���Ϥ�Vo�V�^�	-_���[� �p���#A$�    ��HC������>C�K�����(���Y�[��e
Q�@������`�y����A]�    �̹B��l�ܾ�N�������!x�g�'�	_�	SN���w*���lA��    ���Ľ�Wi��+�Q�y�����������k������ú��_�sx@��@A��    ��|a����
~��T��{��SM��M�o6�ǃ��5�6��q]D��iA�    �hk�ס�����^��������!���yѨ�"�������C�p�/�kAA�    ��Խ�b:����\�~�x���U�'C��x$��(<������iM���A{    �����摇�=��e����t�#��,pRҁG��-r��#'T��h�����A�     ��ƽ�9��#��m�����1�X҅�G�2���(�k�a>�np��"A�0    ����	w�##��u�6����$��7�zҊg��8�I�.p�!ZB�m��%jA&@    ������{�(U�}�C���)=�=+�Ҏ۔�>Ii�3�{�$SE�l���(�A1�    