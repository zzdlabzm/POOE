# POOE
In this work, we use the sequence representations from a pre-trained LPLM (ProtTrans) as input and develop a Support Vector Machine-based method termed as POOE for predicting oomycete effectors. POOE revealed high accuracy for classifying protein sequences as effectors or non-effectors through a 5-fold cross-validation and an independent test.<br>

# Data

**1. train_data**<br>

* positivedata549： 549 oomycete effectors from eight species were regarded as the positive data.<br>
* negativedata549： 549 negative samples were selected from the putative 3337 non-effectors based on the positives to negatives ratios of 1:1.<br>
* negativedata1098： 1098 negative samples were selected from the putative 3337 non-effectors based on the positives to negatives ratios of 1:2.<br>
* negativedata1670： 1670 negative samples were selected from the putative 3337 non-effectors based on the positives to negatives ratios of 1:3.<br>

<table class=MsoTableGrid border=1 cellspacing=0 cellpadding=0 width=0
 style='width:510.35pt;border-collapse:collapse;border:none;mso-border-top-alt:
 solid windowtext .5pt;mso-border-bottom-alt:solid windowtext .5pt;mso-yfti-tbllook:
 1184;mso-padding-alt:0cm 5.4pt 0cm 5.4pt;mso-border-insideh:none;mso-border-insidev:
 none'>
 <tr style='mso-yfti-irow:0;mso-yfti-firstrow:yes;height:22.3pt'>
  <td width=198 rowspan=2 valign=top style='width:148.85pt;border-top:solid windowtext 1.0pt;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:none;
  mso-border-top-alt:solid windowtext .5pt;mso-border-bottom-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:22.3pt'>
  <p class=MsoNormal><span lang=EN-US style='font-size:10.0pt;mso-bidi-font-size:
  10.5pt;font-family:"Times New Roman",serif;mso-fareast-font-family:宋体;
  mso-font-kerning:0pt'>Species<o:p></o:p></span></p>
  </td>
  <td width=95 rowspan=2 valign=top style='width:70.9pt;border-top:solid windowtext 1.0pt;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:none;
  mso-border-top-alt:solid windowtext .5pt;mso-border-bottom-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:22.3pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:10.0pt;mso-bidi-font-size:10.5pt;font-family:"Times New Roman",serif;
  mso-fareast-font-family:宋体;mso-font-kerning:0pt'>Number of positive samples<o:p></o:p></span></p>
  </td>
  <td width=113 rowspan=2 valign=top style='width:3.0cm;border-top:solid windowtext 1.0pt;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:none;
  mso-border-top-alt:solid windowtext .5pt;mso-border-bottom-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:22.3pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:10.0pt;mso-bidi-font-size:10.5pt;font-family:"Times New Roman",serif;
  mso-fareast-font-family:宋体;mso-font-kerning:0pt'>Number of all potential negative
  samples<o:p></o:p></span></p>
  </td>
  <td width=274 colspan=5 style='width:205.55pt;border-top:solid windowtext 1.0pt;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:none;
  mso-border-top-alt:solid windowtext .5pt;mso-border-bottom-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:22.3pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:10.0pt;mso-bidi-font-size:10.5pt;font-family:"Times New Roman",serif;
  mso-fareast-font-family:宋体;mso-font-kerning:0pt'>Number of selected negative
  samples<o:p></o:p></span></p>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:10.0pt;mso-bidi-font-size:10.5pt;font-family:"Times New Roman",serif;
  mso-fareast-font-family:宋体;mso-font-kerning:0pt'><span
  style='mso-spacerun:yes'>&nbsp;</span>(the ratio of positives to negatives)<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:1;height:22.3pt'>
  <td width=91 style='width:68.5pt;border:none;border-bottom:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-top-alt:solid windowtext .5pt;
  mso-border-bottom-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:22.3pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:10.0pt;mso-bidi-font-size:10.5pt;font-family:"Times New Roman",serif;
  mso-fareast-font-family:宋体;mso-font-kerning:0pt'>1:1<o:p></o:p></span></p>
  </td>
  <td width=91 colspan=3 style='width:68.5pt;border-top:solid windowtext 1.0pt;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:none;
  mso-border-top-alt:solid windowtext .5pt;mso-border-bottom-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:22.3pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:10.0pt;mso-bidi-font-size:10.5pt;font-family:"Times New Roman",serif;
  mso-fareast-font-family:宋体;mso-font-kerning:0pt'>1:2<o:p></o:p></span></p>
  </td>
  <td width=91 style='width:68.55pt;border-top:solid windowtext 1.0pt;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:none;
  mso-border-top-alt:solid windowtext .5pt;mso-border-bottom-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:22.3pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:10.0pt;mso-bidi-font-size:10.5pt;font-family:"Times New Roman",serif;
  mso-fareast-font-family:宋体;mso-font-kerning:0pt'>1:3<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:2;height:14.2pt'>
  <td width=198 valign=top style='width:148.85pt;border:none;mso-border-top-alt:
  solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:14.2pt'>
  <p class=MsoNormal><i style='mso-bidi-font-style:normal'><span lang=EN-US
  style='font-size:10.0pt;mso-bidi-font-size:10.5pt;font-family:"Times New Roman",serif;
  mso-fareast-font-family:宋体;mso-font-kerning:0pt'>Phytophthora infestans<o:p></o:p></span></i></p>
  </td>
  <td width=95 valign=top style='width:70.9pt;border:none;mso-border-top-alt:
  solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:14.2pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:10.0pt;mso-bidi-font-size:10.5pt;font-family:"Times New Roman",serif;
  mso-fareast-font-family:宋体;mso-font-kerning:0pt'>180<o:p></o:p></span></p>
  </td>
  <td width=113 valign=top style='width:3.0cm;border:none;mso-border-top-alt:
  solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:14.2pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:10.0pt;mso-bidi-font-size:10.5pt;font-family:"Times New Roman",serif;
  mso-fareast-font-family:宋体;mso-font-kerning:0pt'>373<o:p></o:p></span></p>
  </td>
  <td width=94 colspan=2 valign=top style='width:70.85pt;border:none;
  mso-border-top-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:14.2pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:10.0pt;mso-bidi-font-size:10.5pt;font-family:"Times New Roman",serif;
  mso-fareast-font-family:宋体;mso-font-kerning:0pt'>180<o:p></o:p></span></p>
  </td>
  <td width=85 valign=top style='width:63.8pt;border:none;mso-border-top-alt:
  solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:14.2pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:10.0pt;mso-bidi-font-size:10.5pt;font-family:"Times New Roman",serif;
  mso-fareast-font-family:宋体;mso-font-kerning:0pt'>360<o:p></o:p></span></p>
  </td>
  <td width=95 colspan=2 valign=top style='width:70.9pt;border:none;mso-border-top-alt:
  solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:14.2pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:10.0pt;mso-bidi-font-size:10.5pt;font-family:"Times New Roman",serif;
  mso-fareast-font-family:宋体;mso-font-kerning:0pt'>360<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:3;height:14.2pt'>
  <td width=198 valign=top style='width:148.85pt;border:none;padding:0cm 5.4pt 0cm 5.4pt;
  height:14.2pt'>
  <p class=MsoNormal><i style='mso-bidi-font-style:normal'><span lang=EN-US
  style='font-size:10.0pt;mso-bidi-font-size:10.5pt;font-family:"Times New Roman",serif;
  mso-fareast-font-family:宋体;mso-font-kerning:0pt'>Phytophthora sojae<o:p></o:p></span></i></p>
  </td>
  <td width=95 valign=top style='width:70.9pt;border:none;padding:0cm 5.4pt 0cm 5.4pt;
  height:14.2pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:10.0pt;mso-bidi-font-size:10.5pt;font-family:"Times New Roman",serif;
  mso-fareast-font-family:宋体;mso-font-kerning:0pt'>129<o:p></o:p></span></p>
  </td>
  <td width=113 valign=top style='width:3.0cm;border:none;padding:0cm 5.4pt 0cm 5.4pt;
  height:14.2pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:10.0pt;mso-bidi-font-size:10.5pt;font-family:"Times New Roman",serif;
  mso-fareast-font-family:宋体;mso-font-kerning:0pt'>569<o:p></o:p></span></p>
  </td>
  <td width=94 colspan=2 valign=top style='width:70.85pt;border:none;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.2pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:10.0pt;mso-bidi-font-size:10.5pt;font-family:"Times New Roman",serif;
  mso-fareast-font-family:宋体;mso-font-kerning:0pt'>129<o:p></o:p></span></p>
  </td>
  <td width=85 valign=top style='width:63.8pt;border:none;padding:0cm 5.4pt 0cm 5.4pt;
  height:14.2pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:10.0pt;mso-bidi-font-size:10.5pt;font-family:"Times New Roman",serif;
  mso-fareast-font-family:宋体;mso-font-kerning:0pt'>258<o:p></o:p></span></p>
  </td>
  <td width=95 colspan=2 valign=top style='width:70.9pt;border:none;padding:
  0cm 5.4pt 0cm 5.4pt;height:14.2pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:10.0pt;mso-bidi-font-size:10.5pt;font-family:"Times New Roman",serif;
  mso-fareast-font-family:宋体;mso-font-kerning:0pt'>258<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:4;height:14.2pt'>
  <td width=198 valign=top style='width:148.85pt;border:none;padding:0cm 5.4pt 0cm 5.4pt;
  height:14.2pt'>
  <p class=MsoNormal><i style='mso-bidi-font-style:normal'><span lang=EN-US
  style='font-size:10.0pt;mso-bidi-font-size:10.5pt;font-family:"Times New Roman",serif;
  mso-fareast-font-family:宋体;mso-font-kerning:0pt'>Phytophthora cactorum<o:p></o:p></span></i></p>
  </td>
  <td width=95 valign=top style='width:70.9pt;border:none;padding:0cm 5.4pt 0cm 5.4pt;
  height:14.2pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:10.0pt;mso-bidi-font-size:10.5pt;font-family:"Times New Roman",serif;
  mso-fareast-font-family:宋体;mso-font-kerning:0pt'>126<o:p></o:p></span></p>
  </td>
  <td width=113 valign=top style='width:3.0cm;border:none;padding:0cm 5.4pt 0cm 5.4pt;
  height:14.2pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:10.0pt;mso-bidi-font-size:10.5pt;font-family:"Times New Roman",serif;
  mso-fareast-font-family:宋体;mso-font-kerning:0pt'>508<o:p></o:p></span></p>
  </td>
  <td width=94 colspan=2 valign=top style='width:70.85pt;border:none;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.2pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:10.0pt;mso-bidi-font-size:10.5pt;font-family:"Times New Roman",serif;
  mso-fareast-font-family:宋体;mso-font-kerning:0pt'>126<o:p></o:p></span></p>
  </td>
  <td width=85 valign=top style='width:63.8pt;border:none;padding:0cm 5.4pt 0cm 5.4pt;
  height:14.2pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:10.0pt;mso-bidi-font-size:10.5pt;font-family:"Times New Roman",serif;
  mso-fareast-font-family:宋体;mso-font-kerning:0pt'>252<o:p></o:p></span></p>
  </td>
  <td width=95 colspan=2 valign=top style='width:70.9pt;border:none;padding:
  0cm 5.4pt 0cm 5.4pt;height:14.2pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:10.0pt;mso-bidi-font-size:10.5pt;font-family:"Times New Roman",serif;
  mso-fareast-font-family:宋体;mso-font-kerning:0pt'>252<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:5;height:14.2pt'>
  <td width=198 valign=top style='width:148.85pt;border:none;padding:0cm 5.4pt 0cm 5.4pt;
  height:14.2pt'>
  <p class=MsoNormal><i style='mso-bidi-font-style:normal'><span lang=EN-US
  style='font-size:10.0pt;mso-bidi-font-size:10.5pt;font-family:"Times New Roman",serif;
  mso-fareast-font-family:宋体;mso-font-kerning:0pt'>Plasmopara viticola<o:p></o:p></span></i></p>
  </td>
  <td width=95 valign=top style='width:70.9pt;border:none;padding:0cm 5.4pt 0cm 5.4pt;
  height:14.2pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:10.0pt;mso-bidi-font-size:10.5pt;font-family:"Times New Roman",serif;
  mso-fareast-font-family:宋体;mso-font-kerning:0pt'>38<o:p></o:p></span></p>
  </td>
  <td width=113 valign=top style='width:3.0cm;border:none;padding:0cm 5.4pt 0cm 5.4pt;
  height:14.2pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:10.0pt;mso-bidi-font-size:10.5pt;font-family:"Times New Roman",serif;
  mso-fareast-font-family:宋体;mso-font-kerning:0pt'>396<o:p></o:p></span></p>
  </td>
  <td width=94 colspan=2 valign=top style='width:70.85pt;border:none;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.2pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:10.0pt;mso-bidi-font-size:10.5pt;font-family:"Times New Roman",serif;
  mso-fareast-font-family:宋体;mso-font-kerning:0pt'>38<o:p></o:p></span></p>
  </td>
  <td width=85 valign=top style='width:63.8pt;border:none;padding:0cm 5.4pt 0cm 5.4pt;
  height:14.2pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:10.0pt;mso-bidi-font-size:10.5pt;font-family:"Times New Roman",serif;
  mso-fareast-font-family:宋体;mso-font-kerning:0pt'>76<o:p></o:p></span></p>
  </td>
  <td width=95 colspan=2 valign=top style='width:70.9pt;border:none;padding:
  0cm 5.4pt 0cm 5.4pt;height:14.2pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:10.0pt;mso-bidi-font-size:10.5pt;font-family:"Times New Roman",serif;
  mso-fareast-font-family:宋体;mso-font-kerning:0pt'>190<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:6;height:14.2pt'>
  <td width=198 valign=top style='width:148.85pt;border:none;padding:0cm 5.4pt 0cm 5.4pt;
  height:14.2pt'>
  <p class=MsoNormal><i style='mso-bidi-font-style:normal'><span lang=EN-US
  style='font-size:10.0pt;mso-bidi-font-size:10.5pt;font-family:"Times New Roman",serif;
  mso-fareast-font-family:宋体;mso-font-kerning:0pt'>Hyaloperonospora
  arabidopsidis<o:p></o:p></span></i></p>
  </td>
  <td width=95 valign=top style='width:70.9pt;border:none;padding:0cm 5.4pt 0cm 5.4pt;
  height:14.2pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:10.0pt;mso-bidi-font-size:10.5pt;font-family:"Times New Roman",serif;
  mso-fareast-font-family:宋体;mso-font-kerning:0pt'>33<o:p></o:p></span></p>
  </td>
  <td width=113 valign=top style='width:3.0cm;border:none;padding:0cm 5.4pt 0cm 5.4pt;
  height:14.2pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:10.0pt;mso-bidi-font-size:10.5pt;font-family:"Times New Roman",serif;
  mso-fareast-font-family:宋体;mso-font-kerning:0pt'>304<o:p></o:p></span></p>
  </td>
  <td width=94 colspan=2 valign=top style='width:70.85pt;border:none;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.2pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:10.0pt;mso-bidi-font-size:10.5pt;font-family:"Times New Roman",serif;
  mso-fareast-font-family:宋体;mso-font-kerning:0pt'>33<o:p></o:p></span></p>
  </td>
  <td width=85 valign=top style='width:63.8pt;border:none;padding:0cm 5.4pt 0cm 5.4pt;
  height:14.2pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:10.0pt;mso-bidi-font-size:10.5pt;font-family:"Times New Roman",serif;
  mso-fareast-font-family:宋体;mso-font-kerning:0pt'>66<o:p></o:p></span></p>
  </td>
  <td width=95 colspan=2 valign=top style='width:70.9pt;border:none;padding:
  0cm 5.4pt 0cm 5.4pt;height:14.2pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:10.0pt;mso-bidi-font-size:10.5pt;font-family:"Times New Roman",serif;
  mso-fareast-font-family:宋体;mso-font-kerning:0pt'>165<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:7;height:14.2pt'>
  <td width=198 valign=top style='width:148.85pt;border:none;padding:0cm 5.4pt 0cm 5.4pt;
  height:14.2pt'>
  <p class=MsoNormal><i style='mso-bidi-font-style:normal'><span lang=EN-US
  style='font-size:10.0pt;mso-bidi-font-size:10.5pt;font-family:"Times New Roman",serif;
  mso-fareast-font-family:宋体;mso-font-kerning:0pt'>Bremia lactucae <o:p></o:p></span></i></p>
  </td>
  <td width=95 valign=top style='width:70.9pt;border:none;padding:0cm 5.4pt 0cm 5.4pt;
  height:14.2pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:10.0pt;mso-bidi-font-size:10.5pt;font-family:"Times New Roman",serif;
  mso-fareast-font-family:宋体;mso-font-kerning:0pt'>17<o:p></o:p></span></p>
  </td>
  <td width=113 valign=top style='width:3.0cm;border:none;padding:0cm 5.4pt 0cm 5.4pt;
  height:14.2pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:10.0pt;mso-bidi-font-size:10.5pt;font-family:"Times New Roman",serif;
  mso-fareast-font-family:宋体;mso-font-kerning:0pt'>288<o:p></o:p></span></p>
  </td>
  <td width=94 colspan=2 valign=top style='width:70.85pt;border:none;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.2pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:10.0pt;mso-bidi-font-size:10.5pt;font-family:"Times New Roman",serif;
  mso-fareast-font-family:宋体;mso-font-kerning:0pt'>17<o:p></o:p></span></p>
  </td>
  <td width=85 valign=top style='width:63.8pt;border:none;padding:0cm 5.4pt 0cm 5.4pt;
  height:14.2pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:10.0pt;mso-bidi-font-size:10.5pt;font-family:"Times New Roman",serif;
  mso-fareast-font-family:宋体;mso-font-kerning:0pt'>34<o:p></o:p></span></p>
  </td>
  <td width=95 colspan=2 valign=top style='width:70.9pt;border:none;padding:
  0cm 5.4pt 0cm 5.4pt;height:14.2pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:10.0pt;mso-bidi-font-size:10.5pt;font-family:"Times New Roman",serif;
  mso-fareast-font-family:宋体;mso-font-kerning:0pt'>85<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:8;height:14.2pt'>
  <td width=198 valign=top style='width:148.85pt;border:none;padding:0cm 5.4pt 0cm 5.4pt;
  height:14.2pt'>
  <p class=MsoNormal><i style='mso-bidi-font-style:normal'><span lang=EN-US
  style='font-size:10.0pt;mso-bidi-font-size:10.5pt;font-family:"Times New Roman",serif;
  mso-fareast-font-family:宋体;mso-font-kerning:0pt'>Phytophthora nicotianae<o:p></o:p></span></i></p>
  </td>
  <td width=95 valign=top style='width:70.9pt;border:none;padding:0cm 5.4pt 0cm 5.4pt;
  height:14.2pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:10.0pt;mso-bidi-font-size:10.5pt;font-family:"Times New Roman",serif;
  mso-fareast-font-family:宋体;mso-font-kerning:0pt'>16<o:p></o:p></span></p>
  </td>
  <td width=113 valign=top style='width:3.0cm;border:none;padding:0cm 5.4pt 0cm 5.4pt;
  height:14.2pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:10.0pt;mso-bidi-font-size:10.5pt;font-family:"Times New Roman",serif;
  mso-fareast-font-family:宋体;mso-font-kerning:0pt'>405<o:p></o:p></span></p>
  </td>
  <td width=94 colspan=2 valign=top style='width:70.85pt;border:none;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.2pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:10.0pt;mso-bidi-font-size:10.5pt;font-family:"Times New Roman",serif;
  mso-fareast-font-family:宋体;mso-font-kerning:0pt'>16<o:p></o:p></span></p>
  </td>
  <td width=85 valign=top style='width:63.8pt;border:none;padding:0cm 5.4pt 0cm 5.4pt;
  height:14.2pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:10.0pt;mso-bidi-font-size:10.5pt;font-family:"Times New Roman",serif;
  mso-fareast-font-family:宋体;mso-font-kerning:0pt'>32<o:p></o:p></span></p>
  </td>
  <td width=95 colspan=2 valign=top style='width:70.9pt;border:none;padding:
  0cm 5.4pt 0cm 5.4pt;height:14.2pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:10.0pt;mso-bidi-font-size:10.5pt;font-family:"Times New Roman",serif;
  mso-fareast-font-family:宋体;mso-font-kerning:0pt'>160<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:9;height:5.65pt'>
  <td width=198 valign=top style='width:148.85pt;border:none;border-bottom:
  solid windowtext 1.0pt;mso-border-bottom-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:5.65pt'>
  <p class=MsoNormal><i style='mso-bidi-font-style:normal'><span lang=EN-US
  style='font-size:10.0pt;mso-bidi-font-size:10.5pt;font-family:"Times New Roman",serif;
  mso-fareast-font-family:宋体;mso-font-kerning:0pt'>Phytophthora capsici<o:p></o:p></span></i></p>
  </td>
  <td width=95 valign=top style='width:70.9pt;border:none;border-bottom:solid windowtext 1.0pt;
  mso-border-bottom-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:5.65pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:10.0pt;mso-bidi-font-size:10.5pt;font-family:"Times New Roman",serif;
  mso-fareast-font-family:宋体;mso-font-kerning:0pt'>10<o:p></o:p></span></p>
  </td>
  <td width=113 valign=top style='width:3.0cm;border:none;border-bottom:solid windowtext 1.0pt;
  mso-border-bottom-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:5.65pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:10.0pt;mso-bidi-font-size:10.5pt;font-family:"Times New Roman",serif;
  mso-fareast-font-family:宋体;mso-font-kerning:0pt'>494<o:p></o:p></span></p>
  </td>
  <td width=94 colspan=2 valign=top style='width:70.85pt;border:none;
  border-bottom:solid windowtext 1.0pt;mso-border-bottom-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:5.65pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:10.0pt;mso-bidi-font-size:10.5pt;font-family:"Times New Roman",serif;
  mso-fareast-font-family:宋体;mso-font-kerning:0pt'>10<o:p></o:p></span></p>
  </td>
  <td width=85 valign=top style='width:63.8pt;border:none;border-bottom:solid windowtext 1.0pt;
  mso-border-bottom-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:5.65pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:10.0pt;mso-bidi-font-size:10.5pt;font-family:"Times New Roman",serif;
  mso-fareast-font-family:宋体;mso-font-kerning:0pt'>20<o:p></o:p></span></p>
  </td>
  <td width=95 colspan=2 valign=top style='width:70.9pt;border:none;border-bottom:
  solid windowtext 1.0pt;mso-border-bottom-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:5.65pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:10.0pt;mso-bidi-font-size:10.5pt;font-family:"Times New Roman",serif;
  mso-fareast-font-family:宋体;mso-font-kerning:0pt'>200<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:10;mso-yfti-lastrow:yes;height:20.25pt'>
  <td width=198 valign=top style='width:148.85pt;border:none;border-bottom:
  solid windowtext 1.0pt;mso-border-top-alt:solid windowtext .5pt;mso-border-top-alt:
  solid windowtext .5pt;mso-border-bottom-alt:solid windowtext .5pt;padding:
  0cm 5.4pt 0cm 5.4pt;height:20.25pt'>
  <p class=MsoNormal><span lang=EN-US style='font-size:10.0pt;mso-bidi-font-size:
  10.5pt;font-family:"Times New Roman",serif;mso-fareast-font-family:宋体;
  mso-font-kerning:0pt'>Total<o:p></o:p></span></p>
  </td>
  <td width=95 valign=top style='width:70.9pt;border:none;border-bottom:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-top-alt:solid windowtext .5pt;
  mso-border-bottom-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:20.25pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:10.0pt;mso-bidi-font-size:10.5pt;font-family:"Times New Roman",serif;
  mso-fareast-font-family:宋体;mso-font-kerning:0pt'>549<o:p></o:p></span></p>
  </td>
  <td width=113 valign=top style='width:3.0cm;border:none;border-bottom:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-top-alt:solid windowtext .5pt;
  mso-border-bottom-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:20.25pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:10.0pt;mso-bidi-font-size:10.5pt;font-family:"Times New Roman",serif;
  mso-fareast-font-family:宋体;mso-font-kerning:0pt'>3337<o:p></o:p></span></p>
  </td>
  <td width=94 colspan=2 valign=top style='width:70.85pt;border:none;
  border-bottom:solid windowtext 1.0pt;mso-border-top-alt:solid windowtext .5pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-bottom-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:20.25pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:10.0pt;mso-bidi-font-size:10.5pt;font-family:"Times New Roman",serif;
  mso-fareast-font-family:宋体;mso-font-kerning:0pt'>549<o:p></o:p></span></p>
  </td>
  <td width=85 valign=top style='width:63.8pt;border:none;border-bottom:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-top-alt:solid windowtext .5pt;
  mso-border-bottom-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:20.25pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:10.0pt;mso-bidi-font-size:10.5pt;font-family:"Times New Roman",serif;
  mso-fareast-font-family:宋体;mso-font-kerning:0pt'>1098<o:p></o:p></span></p>
  </td>
  <td width=95 colspan=2 valign=top style='width:70.9pt;border:none;border-bottom:
  solid windowtext 1.0pt;mso-border-top-alt:solid windowtext .5pt;mso-border-top-alt:
  solid windowtext .5pt;mso-border-bottom-alt:solid windowtext .5pt;padding:
  0cm 5.4pt 0cm 5.4pt;height:20.25pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:10.0pt;mso-bidi-font-size:10.5pt;font-family:"Times New Roman",serif;
  mso-fareast-font-family:宋体;mso-font-kerning:0pt'>1670<o:p></o:p></span></p>
  </td>
 </tr>
 <![if !supportMisalignedColumns]>
 <tr height=0>
  <td width=238 style='border:none'></td>
  <td width=113 style='border:none'></td>
  <td width=136 style='border:none'></td>
  <td width=109 style='border:none'></td>
  <td width=4 style='border:none'></td>
  <td width=102 style='border:none'></td>
  <td width=4 style='border:none'></td>
  <td width=109 style='border:none'></td>
 </tr>
 <![endif]>
</table>

**2. additional_data**<br>

* Additional_test_38： 38 effectors from 8 species that were not included in positivedata549 because they were fewer than 10 effectors for individual species.<br>
* Additional_test_29： 29 recently reported effectors (since 2022) that were not included in positivedata549 and additional_test_38.<br>

**3. genome_results**<br>

We used POOE and EffectorO to conduct proteome-wide identification of effectors on *Phytophthora parasitica*. We showed the 324 and 406 effector proteins in *Phytophthora parasitica* and corresponding scores predicted by POOE and EffectorO, respectively.<br>

**4. train_test_seqname**<br>

We showed sequence names of the training and test sets with five-fold cross-validation based on the positives to negatives ratio of 1:3.<br>

# Features
Codes for generating six encoding schemes reported in our POOE article.<br>

**For ESM**<br>
* esm.yaml:  Conda configuration environment for ESM.<br>
* generate_ESM.py:  Script for generating ESM feature.<br>
* example.sh:  Bash code for running generate_ESM.py.<br>

**For ProtTrans**<br>
* prottrans.yaml:  Conda configuration environment for ProtTrans.<br>
* generate_prottrans.py:  Script for generate ProtTrans feature.<br>
* example.sh:  Bash code for running generate_prottrans.py.<br>

# Model
Final prediction models of POOE obtained in 5-fold cross-validation.<br>

# Scripts
* training_SVM: Training and testing code for SVM.
* Run the script.sh, you will get a score and whether it is an oomycete effector. Script description in script.sh: the first parameter represents input fasta, the second one represents temporary folder, and the third one represents specificity. For example：<br>
```Bash
bash ./script.sh input.fasta tmp_dir 0.9
```

# Webserver
The webserver of POOE is freely accessible at http://zzdlab.com/pooe/index.php. 
