CDF   V   
      time             nco_openmp_thread_number            Description       PISMIP6-Greenland recalculated scalar output. Heiko Goelzer 2019, h.goelzer@uu.nl   history      �Wed May 13 12:03:25 2020: ncks -A -v oarea,rhof,rhoi,rhow,dx,dy /home/hgoelzer/Projects/ISMIP6/Archive_sc/Data/SC_GIC1_OBS0//ILTS_PIK/SICOPOLIS2/expb01_05/scalars_mm_GIS_ILTS_PIK_SICOPOLIS2_expb01.nc anc_cr_tmp.nc
Wed May 13 12:03:25 2020: ncap2 -O -s *var_tmp=smb(0); smb=float(smb-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 12:03:24 2020: ncap2 -O -s *var_tmp=sle(0); sle=float(sle-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 12:03:24 2020: ncap2 -O -s *var_tmp=limgr(0); limgr=float(limgr-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 12:03:24 2020: ncap2 -O -s *var_tmp=limfl(0); limfl=float(limfl-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 12:03:24 2020: ncap2 -O -s *var_tmp=limaf(0); limaf=float(limaf-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 12:03:24 2020: ncap2 -O -s *var_tmp=lim(0); lim=float(lim-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 12:03:24 2020: ncap2 -O -s *var_tmp=ivolgr(0); ivolgr=float(ivolgr-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 12:03:24 2020: ncap2 -O -s *var_tmp=ivolfl(0); ivolfl=float(ivolfl-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 12:03:24 2020: ncap2 -O -s *var_tmp=ivol(0); ivol=float(ivol-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 12:03:24 2020: ncap2 -O -s *var_tmp=ivaf(0); ivaf=float(ivaf-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 12:03:24 2020: ncap2 -O -s *var_tmp=iareagr(0); iareagr=float(iareagr-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 12:03:24 2020: ncap2 -O -s *var_tmp=iareafl(0); iareafl=float(iareafl-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 12:03:24 2020: ncap2 -O -s *var_tmp=iarea(0); iarea=float(iarea-var_tmp) anc_cr_tmp0.nc anc_cr_tmp0.nc
Wed May 13 12:03:24 2020: ncdiff -O /home/hgoelzer/Projects/ISMIP6/Archive_sc/Data/SC_GIC1_OBS0//ILTS_PIK/SICOPOLIS2/expb01_05/scalars_mm_GIS_ILTS_PIK_SICOPOLIS2_expb01.nc /home/hgoelzer/Projects/ISMIP6/Archive_sc/Data/SC_GIC1_OBS0//ILTS_PIK/SICOPOLIS2/ctrl_proj_05/scalars_mm_GIS_ILTS_PIK_SICOPOLIS2_ctrl_proj.nc anc_cr_tmp.nc      NCO       "4.6.0"    history_of_appended_files         �Wed May 13 12:03:25 2020: Appended file /home/hgoelzer/Projects/ISMIP6/Archive_sc/Data/SC_GIC1_OBS0//ILTS_PIK/SICOPOLIS2/expb01_05/scalars_mm_GIS_ILTS_PIK_SICOPOLIS2_expb01.nc had no "history" attribute
          smb                 
_FillValue        `�x�   coordinates       lat lon    	long_name         surface mass balance   missing_value         `�x�   units         kg s-1          h   sle                 
_FillValue        `�x�   coordinates       lat lon    	long_name         sealevel equivalent ice mass   missing_value         `�x�   units         m           l   limgr                   
_FillValue        `�x�   coordinates       lat lon    	long_name         grounded ice mass      missing_value         `�x�   units         kg          p   limfl                   
_FillValue        `�x�   coordinates       lat lon    	long_name         floating ice mass      missing_value         `�x�   units         kg          t   limaf                   
_FillValue        `�x�   coordinates       lat lon    	long_name         ice mass above flotation   missing_value         `�x�   units         kg          x   lim                 
_FillValue        `�x�   coordinates       lat lon    	long_name         ice mass   missing_value         `�x�   units         kg          |   ivolgr                  
_FillValue        `�x�   coordinates       lat lon    	long_name         grounded ice volume    missing_value         `�x�   units         m3          �   ivolfl                  
_FillValue        `�x�   coordinates       lat lon    	long_name         floating ice volume    missing_value         `�x�   units         m3          �   ivol                
_FillValue        `�x�   coordinates       lat lon    	long_name         
ice volume     missing_value         `�x�   units         m3          �   ivaf                
_FillValue        `�x�   coordinates       lat lon    	long_name         ice volume above flotation     missing_value         `�x�   units         m3          �   iareagr                 
_FillValue        `�x�   coordinates       lat lon    	long_name         grounded ice sheet area    missing_value         `�x�   units         m2          �   iareafl                 
_FillValue        `�x�   coordinates       lat lon    	long_name         floating ice sheet area    missing_value         `�x�   units         m2          �   iarea                   
_FillValue        `�x�   coordinates       lat lon    	long_name         ice sheet area     missing_value         `�x�   units         m2          �   dx               axis      x      standard_name         projection_x_coordinate    units         m           @   dy               axis      y      standard_name         projection_y_coordinate    units         m           D   oarea                       H   rhof                    P   rhoi                    X   rhow                    `   time                standard_name         time   	long_name         time   bounds        	time_bnds      units         days since 1990-1-1 00:00:00   calendar      360_day    axis      T           �E�@ E�@ B����� @�@     @�p     @�                                                         @��     �:O ��Z�C'6    �Bч�C'6�[��    �[���[9kO�uN    O�uN@¢     J�ɺ�G�4 �    �3�,�4 ��J��    �J���JJwPr    Pr@�V     Jy�к'=�/�b    �/p�/�b�E�,    �E�,�D�O��    O��@�
     �7ེ��V׮c�    ץ��׮c���<�    ��<�Һ�Om�    Om�@ľ     I7�h������f    ��=����f�=�    �=�����O�`    O�`@�r     ������kQ�(�l    �T(�(�l�=��    �=���-���r��    �r��@�&     ���h�T�R�H    �<��R�H�l�A    �l�A�TaU���v    ���v@��     �-���=�؄h�    �n��؄h�Ӕ�D    Ӕ�Dӆ9�O .    O .@ǎ     IД/�K$؎��    �|@؎��Ӡ��    Ӡ��ӏ��O`��    O`��@�B     IJ�`�؝�c    ؍n�؝�cӱO�    ӱO�ӟ&i��K    ��K@��     �\,��%�ضHT    أ��ضHT��1    ��1Ӹ0:Ϯ
    Ϯ
@ɪ     �C}���w����&    ��q���&����    ������1r��'Z    ��'Z@�^     IU:0��&^���    �ԼH�����G    ��G��b�ϰ�    ϰ�@�     J�6��*�� 5+    �◀� 5+�D�    �D����_��c�    ��c�@��     ɔ����C��I    ��b�I�#+�    �#+��  ���)    ���)@�z     �VE.��k�'    ��<�'�<�    �<��#�@��̄    ��̄@�.     I�V)���=�2�f    ��2�f�IG�    �IG��.q��	�8    �	�8@��     �QU2�_��D��    �+���D���]�    �]��A j�0g2    �0g2@Ζ     ʶ龼1v�[%j    �@���[%j�v��    �v���Xͳ�D��    �D��@�J     JuW��l��^��    �Cy}�^���z�?    �z�?�[�m�S�    �S�@��     ʞt�*r��r/3    �V^
�r/3ԈC    ԈC�q8��C$    �C$@�Y     ɷWd�3��~�m    �b"��~�mԏJ�    ԏJ��~w�Q�    �Q�@г     �.���?�ن�    �pQ"ن�ԗ�    ԗ�ԇ6�V_*    �V_*@�     �3�ǼG��ٌ�%    �z��ٌ�%Ԟ/l    Ԟ/lԍ4*�af    �af@�g     ��'�Y(P٘ �    و��٘ �ԫ/F    ԫ/Fԙ��Ќ �    Ќ �@��     �D�Լex-٠\|    ِL�٠\|ԴsS    ԴsSԢ`>ЋU�    ЋU�@�     �kK�n&٦��    ٕ��٦��Իk    ԻkԨ��БG�    БG�@�u     ���p��v�ٳ#    ١�ٳ#�ɔ    �ɔԵΉД�     Д� @��     �#oļ�yaٻ5�    ٩�ٻ5��ҩ�    �ҩ�ԾO��s��    �s��@�)     I(�����ٿ��    ٭��ٿ�����    �����f����    ���@Ӄ     �miM��5~���D    ٴ9���D���j    ���j�ʬk���    ���@��     I�ۅ�������Y    ٸ�?���Y��`�    ��`����#Щ��    Щ��@�7     �%Y����e���    ��j������}w    ��}w�؅oЬLI    ЬLI@ԑ     �3�׼�ae��jq    ��r���jq��?    ��?��Uд�Y    д�Y@��     ʨ��������u    �����u�A�    �A���f��İ�    �İ�@�E     ��#������,    �ޗ���,�	"k    �	"k��z���    ���@՟     �N����?�����    ��5�������    ��� �Q��    ��@��     ʯ8����v    ��J$�v�y|    �y|�2(��8�    ��8�@�S     �,P������o�    ���l�o��g0    �g0��M��!�    ��!�@֭     ʼ�����^]    �/��^]�    ��~����    ���@�     ʫ�̼����    �ʉ���%�L    �%�L��g��J	    ��J	@�a     J (~��:��Pi    �	��Pi�(�    �(��!K�ʄ�    �ʄ�@׻     ���-������    �i����/3    �/3�"��qT    �qT@�     ���0����"��    ���"���7A�    �7A��)�|���    ���@�o     �피�x��*��    ��W�*���@j�    �@j��2���
m�    �
m�@��     ��nӽ~�1��    �%_��1���H:    �H:�:��5�    �5�@�#     �0a�
)��:y�    �-ý�:y��Q�T    �Q�T�C�m�і    �і@�}     ����_}�B�d    �5��B�d�Z�    �Z��LR'�b�    �b�@��     �+�b����K.^    �=�p�K.^�d�t    �d�t�U���5Z    �5Z@�1     � �߽���Sƫ    �F;�Sƫ�nNe    �nNe�^�q�"�@    �"�@@ڋ     �?Ԩ�%�]��    �O�E�]���ys5    �ys5�i��'�v    �'�v@��     � ��+W��f$b    �W~Q�f$bՁ|�    Ձ|��r}C�-L�    �-L�@�?     �o��48��q��    �b���q��Ո"�    Ո"����4�    �4�@ۙ     � /��;q1�{�u    �k���{�uՍ��    Ս��Մ��8S    �8S@��     �ܸ��A|jڂ4    �sW�ڂ4ՒK�    ՒK�Ո���=3&    �=3&@�M     �/���I%mڇB|    �|��ڇB|՘4O    ՘4OՎU��B�    �B�@ܧ     ���OoڋK�    ڂ9sڋK�՜�    ՜�Ւ���H�u    �H�u@�     �Rh�W�Wڐع    ڇ��ڐعբ�     բ� ՘�,�Ml_    �Ml_@�[     �g�Q�`iiږ�    ڍTږ�թ��    թ��՞��R*    �R*@ݵ     ˣQ�k��ڝ�    ڔ �ڝ�ձ�    ձ�զ�"�[bl    �[bl@�     ˀ�n�u�ڤ&    ښrڤ&ո�4    ո�4խa��aA�    �aA�@�i     �t�̽~(Uک�    ڟ��ک�տ:�    տ:�ճ�z�h=h    �h=h@��     ˆ�h���[ڰ2�    ڥ�gڰ2���Eu    ��Euպ���lԒ    �lԒ@�     �9�/���Lڵ7!    ڪ�$ڵ7!����    ������)��q��    �q��@�w     �^�Y��# ں��    ڰ?ں����J+    ��J+��SZ�v�;    �v�;@��     �1����+ڿ�    ڵ �ڿ�����    �����˭��zO�    �zO�@��    ˾C���1]���t    ڼ�����t���P    ���P�Ԏ���	    ��	@�B�    ˺7뽜m����    �Ļ��������[    ���[��`�уRD    уRD@�o�    ��@ͽ�3��ؘ�    ��A7�ؘ����    �������чv    чv@���    �����"���7    ������7���Z    ���Z���2щ�x    щ�x@�ɀ    ˲����W����    ��������i    �i����ь��    ь��@���    ˰c������l    �����l���    ����*я�{    я�{@�#�    ˷$e�������M    �������M���    ������ђli    ђli@�P�    ��܃��V]��v    ������v��    ���
�cѕ<�    ѕ<�@�}�    ˓���� �k1    ����k1�!�    �!���їR�    їR�@᪀    �����N�
z6    ��\�
z6��:    ��:���њN�    њN�@�׀    ��o@��h��Q�    ���Q��!F    �!F�םѝ>    ѝ>@��    ��i��m��=    �L?��=�&�    �&����ѠB�    ѠB�@�1�    ������2O    �p5�2O�,c_    �,c_�$Ȉѣ�c    ѣ�c@�^�    �`���i���    �(�����2�q    �2�q�+8�Ѧ�6    Ѧ�6@⋀    ��N�����$k�    ����$k��9�    �9��1Irѩw�    ѩw�@⸀    �G�S��)��    �"���)���>�a    �>�a�7�Ѭru    Ѭru@��    �:*��#�/�    �(z�/��D�    �D��= �ѯ�&    ѯ�&@��    �{��
�4��    �-��4���KSh    �KSh�Cb�Ѳ    Ѳ@�?�    �$5�����:�Q    �3c��:�Q�Q�    �Q��I��Ѵߧ    Ѵߧ@�l�    