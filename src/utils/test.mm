$c ( $.  

$c ) $.  

$c -> $. 

$c -. $. 

$c wff $.

$c |- $. 

$c & $.  

$c => $. 

$c <-> $.

$c setvar class /\ \/ if- , -/\ \/_  A. = T. F. hadd cadd $.



$v x y A B $.

$v ph $.  

$v ps $.  

$v ch $.  

$v th $.  $( Greek theta $)

$v ta $.  $( Greek tau $)

$v et $.  $( Greek eta $)

$v ze $.  $( Greek zeta $)

$v si $.  $( Greek sigma $)

$v rh $.  $( Greek rho $)

$v mu $.  $( Greek mu $)

$v la $.  $( Greek lambda $)

$v ka $.  $( Greek kappa $)

$v jph $.  $( jarvin Greek phi $)

$v jps $.  $( jarvin Greek psi $)

$v jch $.  $( jarvin Greek chi $)

$v jth $.  $( jarvin Greek theta $)

$v jta $.  $( jarvin Greek tau $)

$v jet $.  $( jarvin Greek eta $)

$v jze $.  $( jarvin Greek zeta $)

$v jsi $.  $( jarvin Greek sigma $)

$v jrh $.  $( jarvin Greek rho $)

$v jmu $.  $( jarvin Greek mu $)

$v jla $.  $( jarvin Greek lambda $)



wjph $f wff jph $.

wjps $f wff jps $.

wjch $f wff jch $.

wjth $f wff jth $.

wjta $f wff jta $.

wjet $f wff jet $.

wjze $f wff jze $.

wjsi $f wff jsi $.

wjrh $f wff jrh $.

wjmu $f wff jmu $.

wjla $f wff jla $.



vx.wal $f setvar x $.

vx.cv $f setvar x $.

wph $f wff ph $.

wps $f wff ps $.

wch $f wff ch $.

wth $f wff th $.

wta $f wff ta $.

wet $f wff et $.

wze $f wff ze $.

wsi $f wff si $.

wrh $f wff rh $.

wmu $f wff mu $.

wla $f wff la $.

wka $f wff ka $.

vx $f setvar x $.

cA $f class A $.

cB $f class B $.

vy $f setvar y $.

${
 
 
 wn $a wff -. ph $.
 
$}

${
 
 
 wi $a wff ( ph -> ps ) $.
 
$}

${
 
 ax-mp.1 $e |- ph $.
 ax-mp.2 $e |- ( ph -> ps ) $.
 
 ax-mp $a |- ps $.
 
$}

${
 
 
 ax-1 $a |- ( ph -> ( ps -> ph ) ) $.
 
$}

${
 
 
 ax-2 $a |- ( ( ph -> ( ps -> ch ) ) -> ( ( ph -> ps ) -> ( ph -> ch ) ) ) $.
 
$}

${
 
 
 ax-3 $a |- ( ( -. ph -> -. ps ) -> ( ps -> ph ) ) $.
 
$}

${
 
 
 wb $a wff ( ph <-> ps ) $.
 
$}

${
 
 
 df-bi $a |- -. ( ( ( ph <-> ps ) -> -. ( ( ph -> ps ) -> -. ( ps -> ph ) ) ) -> -. ( -. ( ( ph -> ps ) -> -. ( ps -> ph ) ) -> ( ph <-> ps ) ) ) $.
 
$}

${
 
 
 wa $a wff ( ph /\ ps ) $.
 
$}

${
 
 
 df-an $a |- ( ( ph /\ ps ) <-> -. ( ph -> -. ps ) ) $.
 
$}

${
 
 
 wo $a wff ( ph \/ ps ) $.
 
$}

${
 
 
 df-or $a |- ( ( ph \/ ps ) <-> ( -. ph -> ps ) ) $.
 
$}

${
 
 
 wif $a wff if- ( ph , ps , ch ) $.
 
$}

${
 
 
 df-ifp $a |- ( if- ( ph , ps , ch ) <-> ( ( ph /\ ps ) \/ ( -. ph /\ ch ) ) ) $.
 
$}

${
 
 
 w3o $a wff ( ph \/ ps \/ ch ) $.
 
$}

${
 
 
 w3a $a wff ( ph /\ ps /\ ch ) $.
 
$}

${
 
 
 df-3or $a |- ( ( ph \/ ps \/ ch ) <-> ( ( ph \/ ps ) \/ ch ) ) $.
 
$}

${
 
 
 df-3an $a |- ( ( ph /\ ps /\ ch ) <-> ( ( ph /\ ps ) /\ ch ) ) $.
 
$}

${
 
 
 wnan $a wff ( ph -/\ ps ) $.
 
$}

${
 
 
 df-nan $a |- ( ( ph -/\ ps ) <-> -. ( ph /\ ps ) ) $.
 
$}

${
 
 
 wxo $a wff ( ph \/_ ps ) $.
 
$}

${
 
 
 df-xor $a |- ( ( ph \/_ ps ) <-> -. ( ph <-> ps ) ) $.
 
$}

${
 
 
 wal $a wff A. x ph $.
 
$}

${
 
 
 cv $a class x $.
 
$}

${
 
 
 wceq $a wff A = B $.
 
$}

${
 
 
 wtru $a wff T. $.
 
$}

${
 
 
 df-tru $a |- ( T. <-> ( A. x x = x -> A. x x = x ) ) $.
 
$}

${
 
 
 wfal $a wff F. $.
 
$}

${
 
 
 df-fal $a |- ( F. <-> -. T. ) $.
 
$}

${
 
 
 whad $a wff hadd ( ph , ps , ch ) $.
 
$}

${
 
 
 df-had $a |- ( hadd ( ph , ps , ch ) <-> ( ( ph \/_ ps ) \/_ ch ) ) $.
 
$}

${
 
 
 wcad $a wff cadd ( ph , ps , ch ) $.
 
$}

${
 
 
 df-cad $a |- ( cadd ( ph , ps , ch ) <-> ( ( ph /\ ps ) \/ ( ch /\ ( ph \/_ ps ) ) ) ) $.
 
$}

${
 
 mp2.1 $e |- ph $.
 mp2.2 $e |- ps $.
 mp2.3 $e |- ( ph -> ( ps -> ch ) ) $.
 
 mp2 $p |- ch $= 
 ( ax-mp wi ) wps wch mp2.2 wph wps wch wi mp2.1 mp2.3 ax-mp ax-mp $. 
$}

${
 
 mp2b.1 $e |- ph $.
 mp2b.2 $e |- ( ph -> ps ) $.
 mp2b.3 $e |- ( ps -> ch ) $.
 
 mp2b $p |- ch $= 
 ( ax-mp ) wps wch wph wps mp2b.1 mp2b.2 ax-mp mp2b.3 ax-mp $. 
$}

${
 
 a1i.1 $e |- ph $.
 
 a1i $p |- ( ps -> ph ) $= 
 ( ax-1 ax-mp wi ) wph wps wph wi a1i.1 wph wps ax-1 ax-mp $. 
$}

${
 
 a2i.1 $e |- ( ph -> ( ps -> ch ) ) $.
 
 a2i $p |- ( ( ph -> ps ) -> ( ph -> ch ) ) $= 
 ( ax-2 ax-mp wi ) wph wps wch wi wi wph wps wi wph wch wi wi a2i.1 wph wps wch ax-2 ax-mp $. 
$}

${
 
 
 idALT $p |- ( ph -> ph ) $= 
 ( ax-1 ax-2 ax-mp wi ) wph wph wph wi wi wph wph wi wph wph ax-1 wph wph wph wi wph wi wi wph wph wph wi wi wph wph wi wi wph wph wph wi ax-1 wph wph wph wi wph ax-2 ax-mp ax-mp $. 
$}

${
 
 
 con4 $p |- ( ( -. ph -> -. ps ) -> ( ps -> ph ) ) $= 
 ( ax-3 ) wph wps ax-3 $. 
$}

${
 
 
 dfbi1ALT $p |- ( ( ph <-> ps ) <-> -. ( ( ph -> ps ) -> -. ( ps -> ph ) ) ) $= 
 ( wch wth ax-1 wb ax-2 ax-3 wi df-bi wn ax-mp ) wph wps wb wph wps wi wps wph wi wn wi wn wi wph wps wi wps wph wi wn wi wn wph wps wb wi wn wi wn wph wps wb wph wps wi wps wph wi wn wi wn wb wph wps df-bi wch wth wch wi wi wph wps wb wph wps wi wps wph wi wn wi wn wi wph wps wi wps wph wi wn wi wn wph wps wb wi wn wi wn wph wps wb wph wps wi wps wph wi wn wi wn wb wi wch wth ax-1 wph wps wb wph wps wi wps wph wi wn wi wn wi wph wps wi wps wph wi wn wi wn wph wps wb wi wn wi wn wph wps wb wph wps wi wps wph wi wn wi wn wb wi wn wch wth wch wi wi wn wi wch wth wch wi wi wph wps wb wph wps wi wps wph wi wn wi wn wi wph wps wi wps wph wi wn wi wn wph wps wb wi wn wi wn wph wps wb wph wps wi wps wph wi wn wi wn wb wi wi wph wps wb wph wps wi wps wph wi wn wi wn wi wph wps wi wps wph wi wn wi wn wph wps wb wi wn wi wn wph wps wb wph wps wi wps wph wi wn wi wn wb wi wn wph wps wb wph wps wi wps wph wi wn wi wn wb wph wps wb wph wps wi wps wph wi wn wi wn wi wph wps wi wps wph wi wn wi wn wph wps wb wi wn wi wn wi wph wps wb wph wps wi wps wph wi wn wi wn wi wph wps wi wps wph wi wn wi wn wph wps wb wi wn wi wn wph wps wb wph wps wi wps wph wi wn wi wn wb wi wn wi wi wph wps wb wph wps wi wps wph wi wn wi wn wi wph wps wi wps wph wi wn wi wn wph wps wb wi wn wi wn wph wps wb wph wps wi wps wph wi wn wi wn wb wi wn wch wth wch wi wi wn wi wph wps wb wph wps wi wps wph wi wn wi wn wi wph wps wi wps wph wi wn wi wn wph wps wb wi wn wi wn wph wps wb wph wps wi wps wph wi wn wi wn wb wi wn wph wps wb wph wps wi wps wph wi wn wi wn wb wph wps wb wph wps wi wps wph wi wn wi wn wi wph wps wi wps wph wi wn wi wn wph wps wb wi wn wi wn wi ax-1 wph wps wb wph wps wi wps wph wi wn wi wn wi wph wps wi wps wph wi wn wi wn wph wps wb wi wn wi wn wph wps wb wph wps wi wps wph wi wn wi wn wb wi wn wph wps wb wph wps wi wps wph wi wn wi wn wb wph wps wb wph wps wi wps wph wi wn wi wn wi wph wps wi wps wph wi wn wi wn wph wps wb wi wn wi wn wi wph wps wb wph wps wi wps wph wi wn wi wn wi wph wps wi wps wph wi wn wi wn wph wps wb wi wn wi wn wph wps wb wph wps wi wps wph wi wn wi wn wb wi wn wi wch wth wch wi wi wn wi wi wph wps wb wph wps wi wps wph wi wn wi wn wi wph wps wi wps wph wi wn wi wn wph wps wb wi wn wi wn wph wps wb wph wps wi wps wph wi wn wi wn wb wi wn wph wps wb wph wps wi wps wph wi wn wi wn wb wph wps wb wph wps wi wps wph wi wn wi wn wi wph wps wi wps wph wi wn wi wn wph wps wb wi wn wi wn wi wph wps wb wph wps wi wps wph wi wn wi wn wi wph wps wi wps wph wi wn wi wn wph wps wb wi wn wi wn wph wps wb wph wps wi wps wph wi wn wi wn wb wi wn wi wi wph wps wb wph wps wi wps wph wi wn wi wn wi wph wps wi wps wph wi wn wi wn wph wps wb wi wn wi wn wph wps wb wph wps wi wps wph wi wn wi wn wb wi wn wch wth wch wi wi wn wi wi wph wps wb wph wps wi wps wph wi wn wi wn wb wph wps wb wph wps wi wps wph wi wn wi wn wi wph wps wi wps wph wi wn wi wn wph wps wb wi wn wi wn wi wph wps wb wph wps wi wps wph wi wn wi wn wi wph wps wi wps wph wi wn wi wn wph wps wb wi wn wi wn wph wps wb wph wps wi wps wph wi wn wi wn wb wi wn wi wch wth wch wi wi wn wi wph wps wb wph wps wi wps wph wi wn wi wn wi wph wps wi wps wph wi wn wi wn wph wps wb wi wn wi wn wph wps wb wph wps wi wps wph wi wn wi wn wb wi wn wph wps wb wph wps wi wps wph wi wn wi wn wb wph wps wb wph wps wi wps wph wi wn wi wn wi wph wps wi wps wph wi wn wi wn wph wps wb wi wn wi wn wi wph wps wb wph wps wi wps wph wi wn wi wn wi wph wps wi wps wph wi wn wi wn wph wps wb wi wn wi wn wph wps wb wph wps wi wps wph wi wn wi wn wb wi wn wi wch wth wch wi wi wn wi wi wch wth wch wi wi wn wn wph wps wb wph wps wi wps wph wi wn wi wn wb wph wps wb wph wps wi wps wph wi wn wi wn wi wph wps wi wps wph wi wn wi wn wph wps wb wi wn wi wn wi wph wps wb wph wps wi wps wph wi wn wi wn wi wph wps wi wps wph wi wn wi wn wph wps wb wi wn wi wn wph wps wb wph wps wi wps wph wi wn wi wn wb wi wn wi wn wi wph wps wb wph wps wi wps wph wi wn wi wn wb wph wps wb wph wps wi wps wph wi wn wi wn wi wph wps wi wps wph wi wn wi wn wph wps wb wi wn wi wn wi wph wps wb wph wps wi wps wph wi wn wi wn wi wph wps wi wps wph wi wn wi wn wph wps wb wi wn wi wn wph wps wb wph wps wi wps wph wi wn wi wn wb wi wn wi wch wth wch wi wi wn wi wph wps wb wph wps wi wps wph wi wn wi wn wb wph wps wb wph wps wi wps wph wi wn wi wn wi wph wps wi wps wph wi wn wi wn wph wps wb wi wn wi wn wi wph wps wb wph wps wi wps wph wi wn wi wn wi wph wps wi wps wph wi wn wi wn wph wps wb wi wn wi wn wph wps wb wph wps wi wps wph wi wn wi wn wb wi wn wi wn wch wth wch wi wi wn wn wph wps wb wph wps wi wps wph wi wn wi wn wb wph wps wb wph wps wi wps wph wi wn wi wn wi wph wps wi wps wph wi wn wi wn wph wps wb wi wn wi wn wi wph wps wb wph wps wi wps wph wi wn wi wn wi wph wps wi wps wph wi wn wi wn wph wps wb wi wn wi wn wph wps wb wph wps wi wps wph wi wn wi wn wb wi wn wi wn wi wph wps wb wph wps wi wps wph wi wn wi wn df-bi wph wps wb wph wps wi wps wph wi wn wi wn wb wph wps wb wph wps wi wps wph wi wn wi wn wi wph wps wi wps wph wi wn wi wn wph wps wb wi wn wi wn wi wph wps wb wph wps wi wps wph wi wn wi wn wi wph wps wi wps wph wi wn wi wn wph wps wb wi wn wi wn wph wps wb wph wps wi wps wph wi wn wi wn wb wi wn wi wn wch wth wch wi wi wn wn ax-1 ax-mp wch wth wch wi wi wn wph wps wb wph wps wi wps wph wi wn wi wn wb wph wps wb wph wps wi wps wph wi wn wi wn wi wph wps wi wps wph wi wn wi wn wph wps wb wi wn wi wn wi wph wps wb wph wps wi wps wph wi wn wi wn wi wph wps wi wps wph wi wn wi wn wph wps wb wi wn wi wn wph wps wb wph wps wi wps wph wi wn wi wn wb wi wn wi ax-3 ax-mp wph wps wb wph wps wi wps wph wi wn wi wn wb wph wps wb wph wps wi wps wph wi wn wi wn wi wph wps wi wps wph wi wn wi wn wph wps wb wi wn wi wn wi wph wps wb wph wps wi wps wph wi wn wi wn wi wph wps wi wps wph wi wn wi wn wph wps wb wi wn wi wn wph wps wb wph wps wi wps wph wi wn wi wn wb wi wn wi wch wth wch wi wi wn wi wph wps wb wph wps wi wps wph wi wn wi wn wi wph wps wi wps wph wi wn wi wn wph wps wb wi wn wi wn wph wps wb wph wps wi wps wph wi wn wi wn wb wi wn ax-1 ax-mp wph wps wb wph wps wi wps wph wi wn wi wn wi wph wps wi wps wph wi wn wi wn wph wps wb wi wn wi wn wph wps wb wph wps wi wps wph wi wn wi wn wb wi wn wph wps wb wph wps wi wps wph wi wn wi wn wb wph wps wb wph wps wi wps wph wi wn wi wn wi wph wps wi wps wph wi wn wi wn wph wps wb wi wn wi wn wi wph wps wb wph wps wi wps wph wi wn wi wn wi wph wps wi wps wph wi wn wi wn wph wps wb wi wn wi wn wph wps wb wph wps wi wps wph wi wn wi wn wb wi wn wi wch wth wch wi wi wn ax-2 ax-mp ax-mp wph wps wb wph wps wi wps wph wi wn wi wn wi wph wps wi wps wph wi wn wi wn wph wps wb wi wn wi wn wph wps wb wph wps wi wps wph wi wn wi wn wb wi wch wth wch wi wi ax-3 ax-mp ax-mp ax-mp $. 
$}

${
 
 
 tbw-ax2 $p |- ( ph -> ( ps -> ph ) ) $= 
 ( ax-1 ) wph wps ax-1 $. 
$}

${
 
 
 weq $p wff x = y $= 
 ( wceq cv ) vx cv vy cv wceq $. 
$}

${
 
 
 tb-ax2 $p |- ( ph -> ( ps -> ph ) ) $= 
 ( ax-1 ) wph wps ax-1 $. 
$}

${
 
 
 bj-0 $p wff ( ( ph -> ps ) -> ch ) $= 
 ( wi ) wph wps wi wch wi $. 
$}

${
 
 wl-impchain-mp-0.1 $e |- ps $.
 wl-impchain-mp-0.2 $e |- ( ps -> ph ) $.
 
 wl-impchain-mp-0 $p |- ph $= 
 ( ax-mp ) wps wph wl-impchain-mp-0.1 wl-impchain-mp-0.2 ax-mp $. 
$}

${
 
 e0a.1 $e |- ph $.
 e0a.2 $e |- ( ph -> ps ) $.
 
 e0a $p |- ps $= 
 ( ax-mp ) wph wps e0a.1 e0a.2 ax-mp $. 
$}

