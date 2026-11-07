# -*- coding: utf-8 -*-
"""Données provisoires de ca-04. Références : support Seddini et PLAN-SOURCE.md.
Le texte, la traduction et les images restent à contrôler avant livraison.
"""

SECTIONS = [
{
'id':'definition', 'nav':'Définition', 'titre':'Définition et deux chiffres', 'source':'Diapositives 3 à 10', 'img':'pression.webp', 'audio':0,
'fr':[
"La pression artérielle (PA) est la pression exercée par le sang sur la paroi des artères. Elle participe à la circulation du sang vers les organes. La mesurer aide au diagnostic et à la surveillance hémodynamique.",
"La pression systolique (PAS) est le chiffre le plus haut et correspond à la contraction cardiaque ; la pression diastolique (PAD) est le plus bas et correspond à la relaxation entre deux contractions.",
"Le cours donne l'exemple 13/8 cmHg, équivalent à 130/80 mmHg : 13 est la systolique, 8 la diastolique. Préciser l'unité évite la confusion."
],
'ar':[
"الضغط الشرياني (<bdi class=\"fr-term\">pression artérielle</bdi>) هو الضغط الذي يمارسه الدم على جدار الشرايين، ويساهم في دوران الدم إلى الأعضاء. قياسه يساعد على التشخيص ومراقبة ديناميكا الدم.",
"الضغط الانقباضي (<bdi class=\"fr-term\">pression systolique</bdi>) هو الرقم الأعلى ويرتبط بانقباض القلب؛ أما الضغط الانبساطي (<bdi class=\"fr-term\">pression diastolique</bdi>) فهو الأدنى ويرتبط باسترخاء القلب بين الانقباضات.",
"مثال الدرس <bdi class=\"fr-plain\">13/8 cmHg</bdi>، وهو يعادل <bdi class=\"fr-plain\">130/80 mmHg</bdi>؛ الأول انقباضي والثاني انبساطي. تحديد الوحدة يمنع الالتباس."
], 'alt':'Coupe schématique d’une artère avec flèches de pression sur sa paroi et sang dans la lumière.'},
{
'id':'variations','nav':'Variabilité','titre':'Variabilité et interprétation','source':'Diapositives 11, 23 à 27','img':'systole.webp','audio':1,
'fr':["La PA augmente transitoirement avec l'effort ou l'émotion et diminue pendant le repos ou le sommeil. Le cours précise qu'elle est souvent plus haute le matin qu'au milieu de l'après-midi. Une élévation ponctuelle ne suffit pas à établir une hypertension permanente.",
"La diapo 23 donne des repères indicatifs de normalité et décrit une hypotension inférieure à 90/50 mmHg. La diapo 24 impose de confronter les chiffres aux valeurs habituelles, aux antécédents, au retentissement clinique et au traitement : un seuil seul ne résume pas la personne.",
"Un résultat obtenu dans de mauvaises conditions peut masquer un défaut de contrôle ou un profil masqué, ou faire évoquer à tort une hypertension blouse blanche. Répéter les mesures est indispensable."],
'ar':["يرتفع الضغط الشرياني مؤقتا مع الجهد أو الانفعال وينخفض في الراحة والنوم. ويذكر الدرس أنه يكون غالبا أعلى صباحا من منتصف بعد الظهر. لا تكفي قراءة مرتفعة عابرة لإثبات ارتفاع دائم.",
"تعطي الشريحة ٢٣ قيما إرشادية وتصف انخفاض الضغط تحت <bdi class=\"fr-plain\">90/50 mmHg</bdi>. وتشدد الشريحة ٢٤ على مقارنة الأرقام بالقيم المعتادة والسوابق والأعراض والعلاج؛ فلا يكفي الحد وحده لتقييم المريض.",
"قد يخفي القياس غير الدقيق سوء الضبط أو النمط المقنع أو يوحي خطأ بنمط المعطف الأبيض. لذلك يجب تكرار القياسات."],
'alt':'Schéma de courbe de pression dans une artère : maximum systolique et minimum diastolique au cours du temps.'},
{
'id':'brassard','nav':'Brassard','titre':'Un brassard adapté au bras','source':'Diapositives 13 à 15 et 30','img':'posture.webp','audio':2,
'fr':["Choisir la taille en fonction de la circonférence et dégager le bras. La poche est placée sur le trajet de l'artère humérale, à hauteur du cœur, avec son bord inférieur au-dessus du pli du coude. Un brassard trop court peut surestimer la PA ; trop large, il peut la sous-estimer.",
"Le support indique environ 2 cm au-dessus du pli à la diapo 15, et au moins 2,5 cm à la diapo 30. La diapo 13 indique largeur de 40 % de la longueur du bras et poche couvrant 80 % de la circonférence.",
"Divergence de formulation : l'American Heart Association exprime la largeur de la poche comme au moins 40 % de la circonférence du bras et sa longueur comme environ 80 % de cette circonférence. Ne pas mélanger longueur du bras et circonférence ; suivre la taille prévue par un appareil validé."],
'ar':["تختار الكفة بحسب محيط الذراع، وتوضع على ذراع مكشوفة، على مسار الشريان العضدي وفي مستوى القلب، وفوق ثنية المرفق. قد تبالغ الكفة القصيرة في النتيجة، وقد تخفضها الكفة الواسعة.",
"تذكر الشريحة ١٥ مسافة تقارب <bdi class=\"fr-plain\">2 cm</bdi> فوق الثنية، بينما تذكر الشريحة ٣٠ ما لا يقل عن <bdi class=\"fr-plain\">2,5 cm</bdi>. وتربط الشريحة ١٣ عرض الكفة بأربعين بالمئة من طول الذراع، وطول الجزء المنفوخ بثمانين بالمئة من محيطها.",
"تختلف صياغة جمعية القلب الأمريكية: عرض الجزء المنفوخ لا يقل عن أربعين بالمئة من محيط الذراع، وطوله نحو ثمانين بالمئة من المحيط. لا نخلط طول الذراع بمحيطها؛ ونتبع مقاس الجهاز المعتمد."],
'alt':'Choix du brassard : mesure de la circonférence du bras et rappel du sens des erreurs de taille.'},
{
'id':'auscultation','nav':'Auscultation','titre':'Méthode auscultatoire','source':'Diapositives 15 à 19 et 30','img':'reel/diapo-16.png','audio':3,
'fr':["Après le repos, placer le stéthoscope sur l'artère humérale au pli du coude, juste en aval du brassard : le pavillon ne doit ni toucher celui-ci ni être glissé dessous. Le cours indique de gonfler jusqu'à abolition du pouls radial puis d'ajouter 20 mmHg.",
"Dégonfler lentement : le premier bruit net repère la systolique ; la disparition des bruits repère habituellement la diastolique. Un trou auscultatoire correspond à une interruption transitoire possible des bruits.",
"Attention à la nomenclature : la diapo 17 appelle « phase 4 » la disparition. L'AHA distingue phase IV = assourdissement et phase V = disparition. L'observation clinique est préservée mais les deux classifications ne sont pas identiques."],
'ar':["بعد الراحة توضع السماعة على الشريان العضدي عند ثنية المرفق، بعد الحافة السفلى للكفة، دون لمسها أو إدخال السماعة تحتها. يذكر الدرس النفخ حتى اختفاء النبض الكعبري ثم إضافة <bdi class=\"fr-plain\">20 mmHg</bdi>.",
"يفرغ الهواء ببطء: أول صوت واضح يحدد الضغط الانقباضي، واختفاء الأصوات يحدد عادة الضغط الانبساطي. وقد تنقطع الأصوات مؤقتا في الفجوة السمعية.",
"اختلاف التسمية: تسمي الشريحة ١٧ الاختفاء المرحلة الرابعة؛ أما جمعية القلب الأمريكية فتسمي خفوت الأصوات المرحلة الرابعة واختفاءها المرحلة الخامسة. لا نخلط بين التسميتين."],
'alt':'Diapositive originale illustrant le brassard et le stéthoscope sur le trajet de l’artère humérale au pli du coude.'},
{
'id':'palpation','nav':'Palpation','titre':'Méthode palpatoire','source':'Diapositives 20 à 22','img':'reel/diapo-20.png','audio':4,
'fr':["Placer les doigts sur le pouls radial puis gonfler. Après disparition du pouls, la diapo 20 décrit 20 mmHg de gonflage supplémentaire. Pendant le dégonflage progressif, la réapparition du pouls repère la systolique.",
"La palpation ne donne pas la diastolique. Elle est utile lorsque l'environnement sonore empêche d'utiliser le stéthoscope. Le cours mentionne aussi poignet, cuisse et cheville comme sites possibles, avec un brassard adapté au site."],
'ar':["توضع الأصابع على النبض الكعبري مع نفخ الكفة. بعد اختفاء النبض تذكر الشريحة ٢٠ زيادة <bdi class=\"fr-plain\">20 mmHg</bdi>. أثناء التفريغ التدريجي يحدد ظهور النبض مجددا الضغط الانقباضي.",
"لا تعطي طريقة الجس الضغط الانبساطي، وقد تفيد عندما تمنع الضوضاء استعمال السماعة. يذكر الدرس إمكان القياس عند الرسغ أو الفخذ أو الكاحل مع اختيار كفة مناسبة للموقع."],
'alt':'Diapositive originale expliquant la méthode palpatoire et le retour du pouls radial au dégonflage.'},
{
'id':'cabinet','nav':'Au cabinet','titre':'Conditions de mesure au cabinet','source':'Diapositives 28 à 30','img':'deux-bras.webp','audio':5,
'fr':["Après plusieurs minutes de repos, assis ou allongé, effectuer au moins deux mesures espacées de quelques minutes et retenir la moyenne des deux dernières selon le support. Lors de la première consultation, mesurer aux deux bras et rechercher une hypotension orthostatique, notamment chez la personne âgée ou diabétique.",
"Le schéma du cours représente dos soutenu, pieds à plat, bras nu soutenu à hauteur du cœur, silence pendant la prise. Il indique 5 minutes de repos, 30 minutes sans effort, 15 minutes sans tabac ni café : ce sont les indications de ce schéma, les protocoles peuvent varier.",
"Le support décrit aussi au cabinet deux mesures par consultation sur trois consultations, soit six mesures sur trois à six mois ; ce calendrier pédagogique ne doit pas être appliqué mécaniquement à une situation urgente."],
'ar':["بعد عدة دقائق راحة جلوسا أو استلقاء، يوصي الدرس بقياسين على الأقل تفصل بينهما دقائق، واعتماد متوسط القياسين الأخيرين. عند أول زيارة يقاس الضغط في الذراعين ويبحث عن انخفاض الضغط الانتصابي خصوصا لدى المسن أو مريض السكري.",
"يظهر رسم الدرس ظهرا مسندا وقدمين مسطحتين وذراعا مكشوفة مسندة بمستوى القلب، مع الصمت أثناء القياس. ويذكر خمس دقائق راحة وثلاثين دقيقة دون جهد وخمس عشرة دون تدخين أو قهوة؛ هذه مدد الرسم وقد تختلف البروتوكولات.",
"يصف الدرس أيضا قياسين في كل من ثلاث زيارات، أي ستة قياسات خلال ثلاثة إلى ستة أشهر؛ ولا يطبق هذا الجدول آليا على حالة إسعافية."],
'alt':'Patient au cabinet avec brassard au bras droit, l’autre bras restant accessible pour une comparaison.'},
{
'id':'erreurs','nav':'Appareils et erreurs','titre':'Appareils, erreurs et différence interbras','source':'Diapositives 31 à 35','img':'comparaison.webp','audio':6,
'fr':["L'appareil oscillométrique estime la PA à partir des oscillations du brassard grâce à un algorithme. Utiliser un appareil validé et contrôlé ; les appareils anéroïdes peuvent se dérégler.",
"Erreurs à éviter : repos insuffisant, brassard inadéquat, gonflage insuffisant, dégonflage rapide, oubli de la mesure aux deux bras ou de la recherche d'hypotension orthostatique.",
"Si la différence dépasse 20 mmHg systoliques et/ou 10 mmHg diastoliques sur trois mesures consécutives, la diapo 34 propose de vérifier simultanément avec deux appareils automatiques. Si elle est confirmée, rechercher une anomalie vasculaire puis utiliser le bras à pression la plus élevée."],
'ar':["يقدر الجهاز التذبذبي (<bdi class=\"fr-term\">oscillométrique</bdi>) الضغط اعتمادا على تذبذبات الكفة وخوارزمية. يستخدم جهاز معتمد ومفحوص، وقد تختل معايرة الجهاز اللاسائلي.",
"الأخطاء: عدم كفاية الراحة، كفة غير مناسبة، نفخ ناقص، تفريغ سريع، ونسيان قياس الذراعين أو البحث عن انخفاض الضغط الانتصابي.",
"عندما يتجاوز الفرق <bdi class=\"fr-plain\">20 mmHg</bdi> انقباضيا و/أو <bdi class=\"fr-plain\">10 mmHg</bdi> انبساطيا في ثلاثة قياسات متتالية، تقترح الشريحة ٣٤ قياسا متزامنا بجهازين. إذا تأكد الفرق يبحث عن سبب وعائي ويستخدم لاحقا الذراع الأعلى ضغطا."],
'alt':'Deux brassards sur les bras d’un patient pour la vérification simultanée d’une différence de pression.'},
{
'id':'automesure','nav':'Automesure','titre':'Mesures hors cabinet : automesure','source':'Diapositives 36 à 41','img':'automesure.webp','audio':7,
'fr':["La confirmation associe au dépistage au cabinet une méthode ambulatoire. L'automesure recourt à un appareil oscillométrique ; la règle des trois du support est trois mesures le matin et trois le soir pendant trois jours consécutifs, assis. Noter les résultats et les remettre au soignant, sans ajuster seul le traitement.",
"Le cours cite des limites : arythmies, troubles cognitifs ou sensoriels, anxiété marquée et évaluation insuffisante de certains appareils chez l'enfant, la femme enceinte ou pour les grands brassards. Les mesures hors cabinet aident à détecter les profils blouse blanche et masqué.",
"Le support cite la mesure hors cabinet avant un traitement antihypertenseur pour confirmer la permanence de l'HTA et rechercher l'effet blouse blanche, ainsi que chez le sujet âgé, en cas d'HTA résistante et pour l'évaluation du traitement. Il indique qu'un plus grand nombre de mesures améliore l'estimation et que ces mesures prédisent mieux le risque de décès cardiovasculaire que la seule pression en consultation."],
'ar':["يجمع تأكيد التقييم بين قياس العيادة وقياس خارجها. يستخدم القياس الذاتي (<bdi class=\"fr-term\">automesure</bdi>) جهازا تذبذبيا؛ وقاعدة الثلاثة في الدرس هي ثلاث قراءات صباحا وثلاث مساء لمدة ثلاثة أيام متتالية جلوسا. تسجل النتائج وتعرض على المهني الصحي دون تغيير العلاج ذاتيا.",
"من الحدود المذكورة اضطراب النظم والاضطرابات المعرفية أو الحسية والقلق الشديد وقلة تقييم بعض الأجهزة عند الأطفال والحوامل أو الكفات الكبيرة. يساعد القياس خارج العيادة على كشف المعطف الأبيض والضغط المقنع.",
"يذكر الدرس القياس خارج العيادة قبل بدء علاج ارتفاع الضغط لتأكيد استمراره والبحث عن أثر المعطف الأبيض، وكذلك عند المسن وفي ارتفاع الضغط المقاوم ولتقييم العلاج. ويرى أن زيادة عدد القياسات تحسن التقدير وأن القياس خارج العيادة يتنبأ بخطر الوفاة القلبية الوعائية أفضل من قياس العيادة وحده."],
'alt':'Patiente à domicile avec brassard au bras relié à un tensiomètre et carnet de mesures sur la table.'},
{
'id':'mapa','nav':'MAPA','titre':'Mesure ambulatoire sur 24 heures','source':'Diapositives 38, 42 et 43','img':'mapa.webp','audio':8,
'fr':["La MAPA est une méthode oscillométrique : un brassard relié à un boîtier portable prend des mesures répétées de jour et de nuit. Le support décrit à titre d'exemple une mesure toutes les 15 minutes le jour et toutes les 45 minutes la nuit. Le protocole réel dépend du dispositif ; pendant la prise, garder le bras détendu et allongé.",
"L'examen apporte de nombreuses mesures hors cabinet et aide à repérer l'hypertension masquée et la blouse blanche. Le cours mentionne la gêne, les pétéchies ou plus rarement un hématome et la difficulté d'interprétation si les mesures sont insuffisantes ou aberrantes."],
'ar':["المراقبة المتنقلة للضغط الشرياني (<bdi class=\"fr-term\">MAPA</bdi>) طريقة تذبذبية: ترتبط الكفة بجهاز محمول يكرر القياس نهارا وليلا. يورد الدرس مثالا كل <bdi class=\"fr-plain\">15</bdi> دقيقة نهارا وكل <bdi class=\"fr-plain\">45</bdi> دقيقة ليلا. يعتمد البروتوكول الفعلي على الجهاز؛ وخلال القياس تبقى الذراع مسترخية وممدودة.",
"توفر المراقبة قراءات كثيرة خارج العيادة وتساعد على كشف الضغط المقنع والمعطف الأبيض. ويذكر الدرس الانزعاج والنمشات ونادرا الورم الدموي وصعوبة التفسير إذا كانت القياسات قليلة أو شاذة."],
'alt':'Patient portant un brassard au bras relié par un tuyau à un enregistreur ambulatoire à la taille.'},
{
'id':'seuils','nav':'Seuils et profils','titre':'Seuils, profils et divergences','source':'Diapositives 23–24 et 44 à 47','img':'reel/diapo-45.png','audio':9,
'fr':["Tableau du cours, seuils d'hypertension : cabinet 140/90 ; automesure 135/85 ; MAPA moyenne 24 h 130/80 ; MAPA de jour 135/85 mmHg. Ces seuils sont atteints si la systolique et/ou la diastolique franchit sa valeur respective.",
"Nuit : la diapo 44 donne une normale inférieure à 120/70, alors que la diapo 45 donne 120/75 comme seuil nocturne. Les recommandations ESH 2023 et ESC 2024 retiennent ≥120 systolique et/ou ≥70 diastolique ; ce sont des références externes distinctes. Faire confirmer la réponse attendue à l'examen.",
"Cabinet élevé et hors cabinet normal : blouse blanche. Cabinet normal et hors cabinet élevé : hypertension masquée. Les deux élevés : hypertension persistante ou non contrôlée sous traitement ; les deux normaux : normotension ou pression contrôlée sous traitement."],
'ar':["جدول الدرس لحدود ارتفاع الضغط: العيادة <bdi class=\"fr-plain\">140/90</bdi>؛ القياس الذاتي <bdi class=\"fr-plain\">135/85</bdi>؛ متوسط المراقبة خلال ٢٤ ساعة <bdi class=\"fr-plain\">130/80</bdi>؛ ونهارا <bdi class=\"fr-plain\">135/85 mmHg</bdi>. يكفي بلوغ الحد الانقباضي و/أو الانبساطي أو تجاوزه.",
"في الليل يوجد اختلاف: تذكر الشريحة ٤٤ أن الطبيعي أقل من <bdi class=\"fr-plain\">120/70</bdi>، وتذكر الشريحة ٤٥ حد <bdi class=\"fr-plain\">120/75</bdi>. التوصيات الأوروبية المستقلة تعتمد عتبة <bdi class=\"fr-plain\">120/70</bdi>؛ وتراجع الأستاذة لمعرفة المطلوب في الامتحان.",
"الضغط مرتفع في العيادة وطبيعي خارجها: المعطف الأبيض؛ طبيعي في العيادة ومرتفع خارجها: الضغط المقنع؛ مرتفع في الحالتين: ارتفاع مستمر أو غير مضبوط بالعلاج؛ طبيعي في الحالتين: ضغط طبيعي أو مضبوط بالعلاج."],
'alt':'Tableau original des seuils d’hypertension selon le contexte de mesure ; le seuil nocturne diffère de la diapositive précédente.'}
]
