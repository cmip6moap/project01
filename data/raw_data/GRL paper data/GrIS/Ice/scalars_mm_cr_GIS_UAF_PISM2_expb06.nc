CDF   V   
      time             nco_openmp_thread_number            Description       PISMIP6-Greenland recalculated scalar output. Heiko Goelzer 2019, h.goelzer@uu.nl   history      �Wed May 13 12:17:04 2020: ncks -A -v oarea,rhof,rhoi,rhow,dx,dy /home/hgoelzer/Projects/ISMIP6/Archive_sc/Data/SC_GIC1_OBS0//UAF/PISM2/expb01_05/scalars_mm_GIS_UAF_PISM2_expb01.nc anc_cr_tmp.nc
Wed May 13 12:17:04 2020: ncap2 -O -s *var_tmp=smb(0); smb=float(smb-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 12:17:04 2020: ncap2 -O -s *var_tmp=sle(0); sle=float(sle-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 12:17:04 2020: ncap2 -O -s *var_tmp=limgr(0); limgr=float(limgr-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 12:17:04 2020: ncap2 -O -s *var_tmp=limfl(0); limfl=float(limfl-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 12:17:04 2020: ncap2 -O -s *var_tmp=limaf(0); limaf=float(limaf-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 12:17:04 2020: ncap2 -O -s *var_tmp=lim(0); lim=float(lim-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 12:17:04 2020: ncap2 -O -s *var_tmp=ivolgr(0); ivolgr=float(ivolgr-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 12:17:04 2020: ncap2 -O -s *var_tmp=ivolfl(0); ivolfl=float(ivolfl-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 12:17:04 2020: ncap2 -O -s *var_tmp=ivol(0); ivol=float(ivol-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 12:17:04 2020: ncap2 -O -s *var_tmp=ivaf(0); ivaf=float(ivaf-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 12:17:04 2020: ncap2 -O -s *var_tmp=iareagr(0); iareagr=float(iareagr-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 12:17:04 2020: ncap2 -O -s *var_tmp=iareafl(0); iareafl=float(iareafl-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 12:17:04 2020: ncap2 -O -s *var_tmp=iarea(0); iarea=float(iarea-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 12:17:03 2020: ncdiff -O /home/hgoelzer/Projects/ISMIP6/Archive_sc/Data/SC_GIC1_OBS0//UAF/PISM2/expb01_05/scalars_mm_GIS_UAF_PISM2_expb01.nc /home/hgoelzer/Projects/ISMIP6/Archive_sc/Data/SC_GIC1_OBS0//UAF/PISM2/ctrl_proj_05/scalars_mm_GIS_UAF_PISM2_ctrl_proj.nc anc_cr_tmp.nc      NCO       "4.6.0"    history_of_appended_files         �Wed May 13 12:17:04 2020: Appended file /home/hgoelzer/Projects/ISMIP6/Archive_sc/Data/SC_GIC1_OBS0//UAF/PISM2/expb01_05/scalars_mm_GIS_UAF_PISM2_expb01.nc had no "history" attribute
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
diagnostic     units         m2          |   dx               axis      x      standard_name         projection_x_coordinate    units         m           $   dy               axis      y      standard_name         projection_y_coordinate    units         m           (   oarea                       ,   rhof                    4   rhoi                    <   rhow                    D   time                standard_name         time   	long_name         time   bounds        	time_bnds      units         days since 2008-1-1 00:00:00   calendar      standard   axis      T           �E�@ E�@ B����� @�@     @�p     @�                                                         @�     �K�й�7���3�=�������	7��U�*����6��e�������mO}@���    JX�{���ׯP
U�׭�ת����F`P"°��0J��_8ί#�L��Ϋ9@��     JD����̴׬��Tн�רF�ש� ��x\O���Ҿ��ҽ[o�h�J����f_m@�z�    �A�K���`״��� ׯ�n׵��˨M���̴*�ų��~�3� �K΀��@��    HE]���	r��&LT���������gm���OŻ=��mΐ��ɛvoΐĚ@Ȝ�    ��g���_��Q�T�9���|n�-��P�P�+���)b�θ��J��θS*@�.     �є��+�B�wU�Z�?�\�@���[9YPp]�XØ�X(���8������	@Ͽ     �=�w�/-��]��UK�t�\Q)�Z�x�yǛPe�v3+�w����O���j@Ѩ     I�-�UI�؇�]Ux�}؆~؅�jӘ�P�Ӗ\�Ӗ���9�R�9z.�9��@�p�    H�$�]?�،��Un�[؋!7؊��ӞIP�;GӜ0/Ӝ�'�4��a���5�@�9@    �C�Z�k��ؖ@pU��:ؔSؓ��өP���Ӧ PӦ���F�lL
K>�D�?@��    �K]���knئԟU� �إH|ؤL�ӻ��P�LDӸ�ӹ�+ς�(K�(ρ�@��@    I����~ػu�U8��ػ��غ����PO�7��R&���ϕ��LTϔ��@ڒ�    I�����J��ʄԫL����u����d����ٱ�����Ϟ��̆5~Ϡ��@�[�    ɱ����w�Ú����&��}�ĚW����ד��;v��˩ϥG�q:�Ϧ�@�$     �j@���s�ԗqS�q���gn��u���9SN�I������#^ϵ>H� �϶L�@��    I�����+v��m�T�7���m���w���QP
���K��FH��0�|eE�ǮE@�ڀ    �V��9���yU gh�����83�\�P4���W��r��%�J/��f@��    ʵҚ���)�
�U���	r�	�S�e�P]n��K�8����L��c��x@�     JgXȻ�~?�!�U0{���q��.�PFk�-��-��*[L�� ��@�@    ʢ���~n�ڑU
����?�O��, �P���+d��*�u�QUK�u!��@�k�    �юȼ}S�)%�Ts���'���(��>VO�Z�>��<��
�rK����
��@�O�    �6�T�O�0�T����/4��0���GSO�P��F�+�E'b��Kx(���@�4     �d�����;�UkrJ�:@�:��SVP�x��RM-�QU=�ՋJ��Y�­@�`    ���c�A,�AyPU�J��?|��@>��Y�P��W�XT�Wy��\1K@�,,@���    �P��'-��T9�Uĺ^�RA��R�F�n��P�_��m �l��� �KyJ6� �Q@��     ���/�i�_{�U���]5��]�P�{z�P�L�y���x��&��K���&+@��@    �����3�,�d��V���bBk�b��Ԁ��Q5����~���&��LA#
�%ߟ@ꩀ    �66��CZ�x#RV
_��uY��u��ԋ��Q��Ԋe-Ԋ<�0�cLj\�0.�@��    H��7�K�4ف�|V8ـ3%ـ�ԑ��Q��Ԑ��ԐB��5�LS3��4.w@�r     ��镼N�jك�ZU��قdق�[Ԕ%�Qxnԓ�ԒR��3ϙLs�n�2�@�V`    I�V<�T��هs�V ��م��نr�ԘlQ��ԗJ�Ԗe��3YkL���1Ն@�:�    �&�W��ى�JVi&ه��و\xԚ�Q$��ԙq�Ԙ��9lL�7�7I1@��    �,%�`%Gُ$�V��ٌ�|َ�ԡ~Q s�ԟҗԞ���@XnM��>m@��    ʝ���h�KٕpV(�Tْoٓ�Qԧ�ZQ=�ԦE Ԥ�=�H�M7�U�E-�@�s�    �����u�Aٝe�V@��ٚ�uٛ��Ա�QY,YԯkPԭ���S�MiYE�O��@���    �G�u���#٦*�VH_�٣0Y٤�Ժ��Qay�Թ8�Է���ZQ\MC��WE@�X     ʪ;1��Q�٩U�V=P�٦jT٧�&Ծ�jQURԼ�YԻCS�`G&M<IP�]V @��     �/+༊��ٱ�0V@OXٮr&ٰ.����QXf���@���L��i��Mc���flI@�<@    ʱՈ��0~ٶ�V4�ٲ��ٴ�����hQK7���N���;�k[�M@���hY@�`    ʪ�����پ�:V?��ٺ��ٽh��e�QW��Ե���W��tb(M[k�p�
@� �    J'~輚����#NVQ$1��_l�ā����QkWm����ڹ�z�Mui��w\@�    ��疼�4���Vd6p������9d����Q�f����]��;��|�wM�d��x5R@��    �����P��-V�%���������!8Q�j��泎��KcЃ�2M��XЁ��@�v�    �gF���k��uV�*�����W��Q�c���1��6Ї��M��Ѕ@��    ��Ԛ�������V����@D���� 2�Q��+���_��8 Ќj$M���Љ�
@�[@    �)�伸����'�V�ޜ��|����n�Q��x����EА,M��1Ѝm�@��`    �K��������V�SJ��)���qs���Q���8��	�Е��M�q=ГQ�@�?�    �'���,���LV���� d�L��Q͆>�~��zЛ��M���И�E@���    �C��Ϝ��yVĊ��s��Od��(Q�)��B��K�У�M�ZcР��@�#�    �9��ޠ��IV�
�����5� z�Q�P�����fШWM�Ф�@���    ����-J�Q�V�r���]����(�Q��]�&��$��Ь��M�(�ЩI@�    �e\���d|���V��������6�-�(R�?�+���*�б�!M�e�Ю�@�z8    �i����"��V������ �n�6��Rջ�4Ɖ�3�Cи�M�;lд�,@��`    �иؽ�U�(�GW\��%��&���=̌R�u�;�F�:H	н��N�6й�I@�^�    �,�q��C�-�V�F�)���+!g�B�9R&��@���>������M���оW�@�Р    �� ���#�3m�W�F�/��1R��I��R���G���E����PHM��@�B�    �M���8�6�W�e�3��4Ă�M��R�*�Ki��I���� �M�ˣ��Ml@���    �\t��;��=��W���:m��;���U�RN��S��Q���́�N)���hJ@�'     ˟h��D��El�WYx�B��B���^(�R.ϔ�[mB�ZS?�Ҕ�N	����F�@��     �x߈�"�L�PAW-g��Lq=�M\��j#,RC ��g��f����N����D@�H    �iwi�)@r�X��W<��T��U�{�s�uRTh��pw��o����\JN/�����@�}p    ˃Uf�/�7�`��WL{0�\���]���|��Rf��yQw�x�G�埨N<m�߿�@��    �2(��6d)�iD�WS�9�ec��e�Ճ>�RnjՁa�Ձ��/N=�}���@�a�    �W��;?,�o^WWU�3�k~��lՆ�|RpN�Մ��Մ�����NC���A@���    �&��@���v��WXR�r���s6�Պ�&Rsk�Ո�OՈ�����ONF�t��s@�F     ˸l½Ek��|)�W^j��xJ��x�0Ս�iRzG�Ջ��Ջ�����NOD���r�@��     ˵�P�N��ڃ�W\8�ځ��ڂ4�Քs�RwϜՒ�YՒD���NS(���}�@�*@    ��P��W�ډ̄W_��ڇ��ڈ�՛�R|]ՙ�՘�@�{�NX�c��1�@��h    �Ї��b�ڐ4�Wd��ڎ0�ڎj�բEHR���ՠBXՠ ����N_ծ�3{A H    ˭ki�l��ږ�8Wl�pڔ�9ڕVթ�]R�P$է�էu��	��Nw9F��A @X    ˪�&�ut�ڜ�-Wp(�ښZ5ښ��հ$5R�?ծ�խ�W��FNp���A yh    ˳嗽}�ڡ��Wr��ڟ��ڟ�fն_R��9ճ��ճ��C�Nw��g�A �|    ��K��l�ڧ	Wq�ڥI�ڥ��ռz�R���պ\չ����eN������A �    ˎ�~����ڮf�Wxy<ڬ �ڬu���?�R����������XoN����+1A$�    ���n��OIڲ�rWt�ڰv�ڰ����rR�������ƒ�S�N}͋�\]A]�    �߫����ں	�Wp��ڷ��ڸ(���X>R�W���:��η/���N}94��A��    ��h�������Wl�hھ�2ڿ8��AsR�7^��,��ևA� `�N|���m�A��    ��z������W����b���%���R�"W�������#��N����D�A�    ��S��ih��S=W�x��̈́���EZ��lKR��7�����C��'�&N����#�AA�    ����i��,�W����7w��&B����R����:>��-��,a�N�.J�( �A{    �	,���K���O�W��)��=��@���ɤR�-1��x���Tn�0�=N�`�+{<A�     ��W������W��������ֱ��)R����������4�EN�܊�/�`A�0    �W���L���:_W�h��������	�uR����v�"�9w�N���3�[A&@    �"���ǭ����(W�� ��!W�����T|R�N5���K��=?�N���7W\AB�    