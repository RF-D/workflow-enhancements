FasdUAS 1.101.10   ��   ��    l   @ ����  O    @    k   ?     	  I   	������
�� .miscactvnull��� ��� null��  ��   	  
  
 l  
 
��������  ��  ��     ��  O   
?    k   >       l   ��  ��    B < Wait for dsync to finish by checking for the temporary file     �   x   W a i t   f o r   d s y n c   t o   f i n i s h   b y   c h e c k i n g   f o r   t h e   t e m p o r a r y   f i l e      r        m       �   
 f a l s e  o      ���� 0 isdone isDone      V    .    k    )      !   I   !�� "��
�� .sysodelanull��� ��� nmbr " m    ���� ��   !  #�� # r   " ) $ % $ I  " '�� &��
�� .sysoexecTEXT���     TEXT & m   " # ' ' � ( ( l t e s t   - f   / t m p / d s y n c _ d o n e   & &   e c h o   ' t r u e '   | |   e c h o   ' f a l s e '��   % o      ���� 0 isdone isDone��    =    ) * ) o    ���� 0 isdone isDone * m     + + � , , 
 f a l s e   - . - l  / /��������  ��  ��   .  / 0 / l  / /�� 1 2��   1 "  Clean up the temporary file    2 � 3 3 8   C l e a n   u p   t h e   t e m p o r a r y   f i l e 0  4 5 4 I  / 4�� 6��
�� .sysoexecTEXT���     TEXT 6 m   / 0 7 7 � 8 8 * r m   - f   / t m p / d s y n c _ d o n e��   5  9 : 9 l  5 5��������  ��  ��   :  ; < ; l  5 5�� = >��   = + % Start packer in the next tab (tab 2)    > � ? ? J   S t a r t   p a c k e r   i n   t h e   n e x t   t a b   ( t a b   2 ) <  @ A @ r   5 ; B C B l  5 9 D���� D 4   5 9�� E
�� 
Trmt E m   7 8���� ��  ��   C o      ���� 0 	secondtab 	secondTab A  F G F O   < U H I H k   @ T J J  K L K I  @ E������
�� .Itrmslctnull���     obj ��  ��   L  M�� M O   F T N O N I  L S���� P
�� .Itrmsntxnull���     obj ��   P �� Q��
�� 
Text Q m   N O R R � S S  p a c k e r��   O 1   F I��
�� 
Wcsn��   I o   < =���� 0 	secondtab 	secondTab G  T U T l  V V��������  ��  ��   U  V W V l  V V�� X Y��   X > 8 Wait for a short delay before starting the next command    Y � Z Z p   W a i t   f o r   a   s h o r t   d e l a y   b e f o r e   s t a r t i n g   t h e   n e x t   c o m m a n d W  [ \ [ I  V [�� ]��
�� .sysodelanull��� ��� nmbr ] m   V W���� ��   \  ^ _ ^ l  \ \��������  ��  ��   _  ` a ` l  \ \�� b c��   b ( " Start web in the next tab (tab 3)    c � d d D   S t a r t   w e b   i n   t h e   n e x t   t a b   ( t a b   3 ) a  e f e r   \ d g h g l  \ ` i���� i 4   \ `�� j
�� 
Trmt j m   ^ _���� ��  ��   h o      ���� 0 thirdtab thirdTab f  k l k O   e � m n m k   k � o o  p q p I  k p������
�� .Itrmslctnull���     obj ��  ��   q  r�� r O   q � s t s I  w ����� u
�� .Itrmsntxnull���     obj ��   u �� v��
�� 
Text v m   y | w w � x x  w e b��   t 1   q t��
�� 
Wcsn��   n o   e h���� 0 thirdtab thirdTab l  y z y l  � ���������  ��  ��   z  { | { l  � ��� } ~��   } < 6 Delay to ensure previous command initializes properly    ~ �   l   D e l a y   t o   e n s u r e   p r e v i o u s   c o m m a n d   i n i t i a l i z e s   p r o p e r l y |  � � � I  � ��� ���
�� .sysodelanull��� ��� nmbr � m   � ����� ��   �  � � � l  � ���������  ��  ��   �  � � � l  � ��� � ���   � H B Check if the cloudflared process is running using a shell command    � � � � �   C h e c k   i f   t h e   c l o u d f l a r e d   p r o c e s s   i s   r u n n i n g   u s i n g   a   s h e l l   c o m m a n d �  � � � r   � � � � � m   � ���
�� boovfals � o      ���� 0 cloudrunning cloudRunning �  � � � Q   � � � � � � k   � � � �  � � � r   � � � � � I  � ��� ���
�� .sysoexecTEXT���     TEXT � m   � � � � � � � B p g r e p   - f   ' c l o u d f l a r e d   t u n n e l   r u n '��   � o      ���� (0 cloudflaredprocess cloudflaredProcess �  ��� � Z   � � � ����� � >  � � � � � o   � ����� (0 cloudflaredprocess cloudflaredProcess � m   � � � � � � �   � r   � � � � � m   � ���
�� boovtrue � o      ���� 0 cloudrunning cloudRunning��  ��  ��   � R      ������
�� .ascrerr ****      � ****��  ��   � k   � � � �  � � � l  � ��� � ���   � ? 9 Ignore the error if the cloudflared process is not found    � � � � r   I g n o r e   t h e   e r r o r   i f   t h e   c l o u d f l a r e d   p r o c e s s   i s   n o t   f o u n d �  ��� � r   � � � � � m   � ���
�� boovfals � o      ���� 0 cloudrunning cloudRunning��   �  � � � l  � ���������  ��  ��   �  � � � l  � ��� � ���   � O I If the cloud tunnels are not running, start them in the next tab (tab 4)    � � � � �   I f   t h e   c l o u d   t u n n e l s   a r e   n o t   r u n n i n g ,   s t a r t   t h e m   i n   t h e   n e x t   t a b   ( t a b   4 ) �  � � � Z   �& � ����� � H   � � � � o   � ����� 0 cloudrunning cloudRunning � k   �" � �  � � � r   � � � � � l  � � ����� � 4   � ��� �
�� 
Trmt � m   � ����� ��  ��   � o      ���� 0 cloudtab cloudTab �  ��� � Z   �" � ��� � � I  � ��� ���
�� .coredoexnull���     obj  � o   � ����� 0 cloudtab cloudTab��   � O   � � � � � k   � � � �  � � � I  � �������
�� .Itrmslctnull���     obj ��  ��   �  ��� � O   � � � � � I  � ����� �
�� .Itrmsntxnull���     obj ��   � �� ���
�� 
Text � m   � � � � � � � 
 c l o u d��   � 1   � ���
�� 
Wcsn��   � o   � ����� 0 cloudtab cloudTab��   � k   �" � �  � � � r   � � � � l  �  ���� � I  � �~�}�|
�~ .Itrmntwnnull���     obj �}  �|  ��  �   � o      �{�{ 0 cloudtab cloudTab �  ��z � O  " � � � k  ! � �  � � � I �y�x�w
�y .Itrmslctnull���     obj �x  �w   �  ��v � O  ! � � � I  �u�t �
�u .Itrmsntxnull���     obj �t   � �s ��r
�s 
Text � m   � � � � � 
 c l o u d�r   � 1  �q
�q 
Wcsn�v   � o  �p�p 0 cloudtab cloudTab�z  ��  ��  ��   �  � � � l ''�o�n�m�o  �n  �m   �  � � � l ''�l � ��l   �   Display the result    � � � � &   D i s p l a y   t h e   r e s u l t �  ��k � Z  '> � ��j � � o  '*�i�i 0 cloudrunning cloudRunning � I -4�h ��g
�h .sysodisAaleR        TEXT � m  -0 � � � � � 4 C l o u d   t u n n e l s   a r e   r u n n i n g .�g  �j   � I 7>�f ��e
�f .sysodisAaleR        TEXT � m  7: � � � � � ~ C l o u d   t u n n e l s   a r e   n o t   r u n n i n g .   S t a r t i n g   c l o u d   c o m m a n d   i n   t a b   4 .�e  �k    1   
 �d
�d 
Crwn��    m      � �|                                                                                  ITRM  alis      Macintosh HD               �!:3BD ����	iTerm.app                                                      �����R        ����  
 cu             Applications  /:Applications:iTerm.app/    	 i T e r m . a p p    M a c i n t o s h   H D  Applications/iTerm.app  / ��  ��  ��       �c � ��c   � �b
�b .aevtoappnull  �   � **** � �a ��`�_ � ��^
�a .aevtoappnull  �   � **** � k    @ � �  �]�]  �`  �_   �   � " ��\�[ �Z +�Y '�X 7�W�V�U�T�S R�R�Q w�P ��O ��N�M�L�K�J ��I � ��H �
�\ .miscactvnull��� ��� null
�[ 
Crwn�Z 0 isdone isDone
�Y .sysodelanull��� ��� nmbr
�X .sysoexecTEXT���     TEXT
�W 
Trmt�V 0 	secondtab 	secondTab
�U .Itrmslctnull���     obj 
�T 
Wcsn
�S 
Text
�R .Itrmsntxnull���     obj �Q 0 thirdtab thirdTab�P 0 cloudrunning cloudRunning�O (0 cloudflaredprocess cloudflaredProcess�N  �M  �L �K 0 cloudtab cloudTab
�J .coredoexnull���     obj 
�I .Itrmntwnnull���     obj 
�H .sysodisAaleR        TEXT�^A�=*j O*�,0�E�O h�� kj O�j E�[OY��O�j O*�l/E�O� *j O*�, 	*��l UUOkj O*�m/E` O_  *j O*�, *�a l UUOkj OfE` O $a j E` O_ a  
eE` Y hW X  fE` O_  a*�a /E` O_ j  "_  *j O*�, *�a l UUY )*j E` O_  *j O*�, *�a l UUY hO_  a j  Y 	a !j  UU ascr  ��ޭ