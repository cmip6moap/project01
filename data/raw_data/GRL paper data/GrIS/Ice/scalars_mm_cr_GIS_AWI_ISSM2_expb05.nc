CDF   V   
      time             nco_openmp_thread_number            Description       PISMIP6-Greenland recalculated scalar output. Heiko Goelzer 2019, h.goelzer@uu.nl   history      �Wed May 13 11:57:58 2020: ncks -A -v oarea,rhof,rhoi,rhow,dx,dy /home/hgoelzer/Projects/ISMIP6/Archive_sc/Data/SC_GIC1_OBS0//AWI/ISSM2/expb05_05/scalars_mm_GIS_AWI_ISSM2_expb05.nc anc_cr_tmp.nc
Wed May 13 11:57:58 2020: ncap2 -O -s *var_tmp=smb(0); smb=float(smb-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 11:57:58 2020: ncap2 -O -s *var_tmp=sle(0); sle=float(sle-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 11:57:58 2020: ncap2 -O -s *var_tmp=limgr(0); limgr=float(limgr-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 11:57:58 2020: ncap2 -O -s *var_tmp=limfl(0); limfl=float(limfl-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 11:57:58 2020: ncap2 -O -s *var_tmp=limaf(0); limaf=float(limaf-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 11:57:58 2020: ncap2 -O -s *var_tmp=lim(0); lim=float(lim-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 11:57:58 2020: ncap2 -O -s *var_tmp=ivolgr(0); ivolgr=float(ivolgr-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 11:57:58 2020: ncap2 -O -s *var_tmp=ivolfl(0); ivolfl=float(ivolfl-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 11:57:58 2020: ncap2 -O -s *var_tmp=ivol(0); ivol=float(ivol-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 11:57:58 2020: ncap2 -O -s *var_tmp=ivaf(0); ivaf=float(ivaf-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 11:57:58 2020: ncap2 -O -s *var_tmp=iareagr(0); iareagr=float(iareagr-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 11:57:58 2020: ncap2 -O -s *var_tmp=iareafl(0); iareafl=float(iareafl-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 11:57:58 2020: ncap2 -O -s *var_tmp=iarea(0); iarea=float(iarea-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 11:57:57 2020: ncdiff -O /home/hgoelzer/Projects/ISMIP6/Archive_sc/Data/SC_GIC1_OBS0//AWI/ISSM2/expb05_05/scalars_mm_GIS_AWI_ISSM2_expb05.nc /home/hgoelzer/Projects/ISMIP6/Archive_sc/Data/SC_GIC1_OBS0//AWI/ISSM2/ctrl_proj_05/scalars_mm_GIS_AWI_ISSM2_ctrl_proj.nc anc_cr_tmp.nc      NCO       "4.6.0"    history_of_appended_files         �Wed May 13 11:57:58 2020: Appended file /home/hgoelzer/Projects/ISMIP6/Archive_sc/Data/SC_GIC1_OBS0//AWI/ISSM2/expb05_05/scalars_mm_GIS_AWI_ISSM2_expb05.nc had no "history" attribute
          smb                 comment       9Surface Mass Balance flux (for areas covered by ice only)      coordinates       lat lon    	long_name         surface mass balance   units         kg s-1          x   sle                 comment       The thickness of the ice sheet     coordinates       lat lon    	long_name         sealevel equivalent ice mass   units         m           |   limgr                   comment       The thickness of the ice sheet     coordinates       lat lon    	long_name         grounded ice mass      units         kg          �   limfl                   comment       The thickness of the ice sheet     coordinates       lat lon    	long_name         floating ice mass      units         kg          �   limaf                   comment       The thickness of the ice sheet     coordinates       lat lon    	long_name         ice mass above flotation   units         kg          �   lim                 comment       The thickness of the ice sheet     coordinates       lat lon    	long_name         ice mass   units         kg          �   ivolgr                  comment       The thickness of the ice sheet     coordinates       lat lon    	long_name         grounded ice volume    units         m3          �   ivolfl                  comment       The thickness of the ice sheet     coordinates       lat lon    	long_name         floating ice volume    units         m3          �   ivol                comment       The thickness of the ice sheet     coordinates       lat lon    	long_name         
ice volume     units         m3          �   ivaf                comment       The thickness of the ice sheet     coordinates       lat lon    	long_name         ice volume above flotation     units         m3          �   iareagr                 comment       �Fraction of grid cell covered by grounded ice sheet, where grounded indicates that the quantity correspond to the ice sheet that flows over bedrock    coordinates       lat lon    	long_name         grounded ice sheet area    units         m2          �   iareafl                 comment       @Fraction of grid cell covered by ice sheet flowing over seawater   coordinates       lat lon    	long_name         floating ice sheet area    units         m2          �   iarea                   comment       RFraction of grid cell covered by land ice (ice sheet, ice shelf, ice cap, glacier)     coordinates       lat lon    	long_name         ice sheet area     units         m2          �   dx               axis      x      standard_name         projection_x_coordinate    units         m           P   dy               axis      y      standard_name         projection_y_coordinate    units         m           T   oarea                       X   rhof                    `   rhoi                    h   rhow                    p   time                standard_name         time   bounds        	time_bnds      units         days since 1990-1-1 00:00:00   calendar      365_day    axis      T           �E�@ E�@ B����� @�@     @�p     @�@                                                         @     I��� 80�G�w�"�^�I��J��`��6�z�c[��b�PȎpH�p    @�?�    �&�ӹ������Ӛt�֩�C��v����έ�^���Ѿ���H�J�`��7��@��     J���2���t����$��`��vF�҉���wbҊ���|��̇��In�̍f@Ĭ�    J����B�,׆�Ӆ���t��ׇS�җ�CΖT[ҘG�҉��
�;�����@�c     HC��:"�\v)Ԍ��A���`֧�xoϝ���}L�ZDF�4��˼��Lew@��    ���$�h)�צղ�+ב�Nק�һ�%�$z�ҼbҤH]�h��,b�͕@�@��     ʜ�>��{#��.��1�׿���L����I�!!������˫͋��� �T͛�@ǆ�    �nlV��s��'#��4����)d��<1�"E`�>�F�,E7͕�*̤��Ϳ@�=     I�.X� ��]�5�j���Jv-�az�y��Є2��}�)�c�0ͩ`0�&�����@��    �v��)t�j���oq�U��l�rӄ��)G�ӅU5�oл�٩c�d~��%�`@ɪ     H,⫻L�(؋��1�`؀�m،hӜoZ�Gԉӝ�Ӑ؉����xY��(�a@�`�    �PF�Z�rؕW^�@��؉y�ؖ�tӨ��X��ө�Ӛ����O�͒�a�7�@�     IĩM���شN�Ջm�ا+ض|b���.М�T��X�Ӽ.�ʹͨ!��Uފ@�̀    �"���	�ؼ5n��ح��ؽj����X�.$��%���[O�&ͽ�=�y%@̄     �9,���	��{��͍v��Br��Ib�����M���F��xX��|;�>�|��@�:�    ʁ����o��岥�����Z�����<���0K�����4��3�ͩ�΄v�@��     �	@���u��LŇ���r�BJ��b�fl�����	��R XͷxJΖ�>@Χ�    H���˛��*�;Z� ��	e������9���g�ͬW�Ξ��@�^     �(K��� (�������V�pL� ��� �]�!hl����s8���C�ή-^@�
@    ʍ�I��n��Yտ�����yC�.cj���0l�$:��z'���λ�@�e�    H�y������(�f��ϲ��M�*5�=����׶�?���3�Ήi� h��ɝo@���    Hذ��})�/��ճ(��&���1\��F��ɚ��G��;��Δ����N����@�     H]m��	_h�7*յq0�,�'�8r�M����,�O�G�Bi�δ@���`��%~@�w@    ���ܼu��<-Cտ��1��=�x�S�'��N�Un>�H2�ζ��cf����@�Ҁ    ʏ�Uw�O���؋��D���Q;��i����D�kq��]?����(�	�~�k�@�-�    �:��'���^ m��0��S��_���y�� ��{���m����y��
�H��n@҉     ���.�8��r����+��g���tg	Ԉ}L���ԉ��ԂG���R�]�	 M@��@    �*t��FB<ق{n����yXOك`#Ԓ�	� ��ԓ�eԌJq���x����:@�?�    �vr\�O>�و.���قR�ىԙ>s��w�Ԛ=�Ԓ�l��:���\���@Ӛ�    ʂ�&�[Yِ'���K�ى�ّ�Ԣ6���-ԣHoԛ6���r���H�@��     H�`�h��ٙB����uْAgٚ,qԬu���;ԭ|�Ԥ���;h����_@�Q@    ɧg��o6�ٝ�3��܋ٖmDٞ�Աt�� 4ԲuԩE��
��؅B�"�@Ԭ�    ��t�w��٣da����ٛ��٤_�Է�k��nԸ�yԯ1�������M�'Y!@��    ʐ#0���qٯ�<��
٨�ٱ�����!׉��/�Խ`�M����K�3�@�c     ��D����fٻʛ�tٲh�ٽ���Q#�0���Բ����#Z�t�Hw@վ@    �lդ���r����,ٸ����U��if�1�����`�ϯ��*�.���N�R@��    ʉK`���$��h2��F���̧�����3����K ��D!�/����S�@�t�    ��.���Q���p��;���ɡ�������S������n�0#l�#[��X�X@��     �B�x��D����O�C?�Ӡy��QN���D�[����k>��#j�/���Dm�U�@�+@    �i����E��!��=��Y����s�T�e��2� z�<a����])@׆�    ɌVY��)� 5��L����@���E��fl$�,	����K�6�,t�rOS@���    �O/T��<6����N������P����g� �k��T�XH;� Úπ<�@�=     �������k�T��2��@�W�o�T�����s�Y�����π<�@ؘ@    �+<}��'��-��j������'��у���(�[�R��f��"W�χ�R@��    ʇ���W�QCւ:�y��Ul�,�4ђ_��-���#�&�r��$݆ύ��@�N�    �H������x�:���Il�hc�2�O�RV��3`��),�d���ϐ�M@٪     �Qd���Ձ�(��4Q�����)Cq�=���J��>w��3��σ_���*ϓ��@�@    �/����
�1&��=l��("��1��GW��U'g�H-#�=2�σ��Q�ϗ1@�`�    �>U���9���7R�0/��:L��P�N�N
}�Q�Y�FBϊ�qϜ�@ڻ�    �W������@���=���77��A���Y-�U���Y���N+[Ϗt��T�ϡ�@�     ʉ�F���I�K�:�p�@#��J���c"��R ~�c���X5�ϒ���4sϤ�c@�r@    �g3����N�D�?-h�E!M�O�q�h���W ��i���]�TϚ���\Ϭ��@�̀    ˖0b�% ��Y���;U��O���Z��u ��Rͯ�u��i��Ϡ)����ϲ|�@�(�    �?Lw�.���fc_�4���[��g�Ձ� �K4�Ղ��wNAϨva��)ϻ-�@܄     ʪ+ͽ5�9�o_)�3�w�d}w�p�Ն���JfՇ�Հ��ϫ����.Ͼ]�@��@    �%��9�!�t��J	��i��u�Չ�U�cYDՊ1Ճ�ϯ���Q���@�:�    �'W�@/1�}>�D���q���}��Վh��]T�Վ�tՇ�ϵ >�n���.@ݕ�    ˅�;�I0{ڄt��K�X�}�ڄڈՕ��e`�Օ1Վ]TϻMk�$r��۫@��     �L��Q��ډѲ֎ڃ�Uڊ_�՛�џ�8՛��Քp�ϼی�?]z���<@�L@    ˄,��Y-�ڎ��֝��ڈ��ڏG�ՠ��ѱ�Xա:�ՙ������E���ٿ�@ާ�    �%�}�b0jڔ�D֕��ڎ<tڕ4է<�Ѩ�<է�ՠ��5�BJ���~\@��    �3q��h�8ڙ�և(ڒ_Kڙ��լ=wјլՀդ������;���i�@�^     �@���p��ڞ;nք�ڗD[ڞ��ղ�є�ղ��ժ7���uU�C�N����@߹@    �f]�wf�ڢ���w��ڛ�,ڣVշAыYmշ��կ���I�HG1��Q�@�
@    ˫ ����ڧ�
�b�8ڠ�<ڨ^Xռ�{�~��սu�մ�����L���t@�7�    ˘fV���ڮ���a��ڧ^Mگ
���yv�}����hռU����; ��bo@�e�    ˤiI��*ڵ;��tkڭ�ڵ�"���)щ����y��È����\�]��I�@��     ˱c�����ڼ^ևNiڴz�ڼ���Ӫ�јA���C&������f�1�,�@���    ˨?�����_,ֆ�\ڻwT��������ї����p\���n���4�l���
@�@��`    ˀ3���$"����ք߀�����_���$�ѕ������%#�����p�����@�     ˸�O���%���֓�?�ǤM�Р����Ѧa���D�����h
΃*��V@�I�    ˢt���P���5e֒c��Χ�������+4Ѥ����������΅�8�:�@�w@    �ρ ������֍R��E��ި]���џE���������S΄�8�{:@��    ��i��ˏ���ևD������>�jSј7��n���[��/΂w �@�Ҁ    ���ӽ�������ֆ������*}��qї��� G� �H�	���z��"�@�      ˯����Ӑ��o�sG���9x����
ш���
[����͡�t�8�5@�-�    ��sн���"d�k�Z���5���D��6ф��������l�j����@�[`    ˡ�����N^�_u*��O��;��S�{s���0�eU�F�[����@�     ��S��̫��["�s�T� ������щ��Tw��-�/f΁��QD@ⶠ    �	���Ҁ�	��]�k�^��	G�;-�y�1�y������q����@��@    ����Ud��K.V�	K��C���'�d�k� P�~����y�8�"�L@��    ����������������%���3�)�&,�� �b�	��t88�$ML@�?�    � A��Ǽ�O��(G�a��y��*Dd�=B�*s��$���y��x��&�@�m     ��i��@�����T�������0:�#���0b��*�����m���&��@��    ��涽��M� C� P��� K�4V����4_��.������C$B�&��@��`    