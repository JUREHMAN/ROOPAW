#Importing the root
import ROOT
from ROOT import gROOT
from ROOT import TCanvas, TPad, TFile, TPaveLabel, TPaveText, THStack
from ROOT import TLegend
##Opening the signal file
#fs = TFile("incl_1M_with_mva_cuts.root")
fs = TFile("belle_data_all_exp.root")
%get inclall sig

fmc = TFile("control_channel_fullsample_newangle.root")
%get inclall mc

#Sum of the cos angle on tag side and the cos b/w the tag side visible momentum and momentun on the signal side(for control channel only)
%form sum_cos_tag_sig_momentum cos_pBtag_Dltag+cos_theta_pBsig_ptagvis

#Forming the possible solutions
%form s1 sum_ang1_plus_tag
%form s2 sum_ang2_plus_tag

#Minimum of the absolute value
%form min_abs_value min(abs(s1),abs(s2))

#Maximum value
%form max_value max((s1),(s2))

#Maximum absolute value
%form max_abs_value max(abs(s1),abs(s2))

#Checking if max. absolute value is equal to the max. value or not 
%form is_equal max_value == max_abs_value

#it will return either 0 or 1
%form sign ((is_equal)-0.5)*2

#For preserving the inital sign(+ or -)
%form tot_ch (s1*s2)/(abs(s1*s2))

#Best solution
%form best_soln  sign*tot_ch*min_abs_value

#Bad solution
%form bad_soln sign*max_abs_value

#Defining the cuts
%cut m_Dcut abs(m_D-1.86)<0.015
%cut cos_cut abs(cos_pBtag_Dltag)<1
%cut Ycut Yincl_rank_all==1
%cut sin_cut abs(sin_phi)<1
%cut jpsi_cut abs(m_Jpsi-3.1)<0.02
%cut Mbc_sig_cut Mbc_Bsig>5.27
%cut deltaE_sig_cut1 deltaE_Bsig>-0.050
%cut deltaE_sig_cut2 deltaE_Bsig<0.050
#%cut all_sig_side_cut Ycut&&Mbc_sig_cut&&deltaE_sig_cut1&&deltaE_sig_cut2
%cut all_sig_side_cut Ycut&&Mbc_sig_cut&&deltaE_sig_cut1&&deltaE_sig_cut2&&sin_cut
%cut add_cut sin_cut

#Defining the histograms for best solutions  -0.15<deltaE_Bsig<0.050
%1d h1 100 -3 3
%1d h2 100 -3 3

#Best solution plot preperation
%ntpl mc best_soln all_sig_side_cut h1
%ntpl mc sum_cos_tag_sig_momentum all_sig_side_cut h2 


#Normalizing the mc hist
#h2.Scale(1.0 / h1.Integral(),"width");

#Setting the title   cos(PBvistag,PBsig)+cos(PBtag,PBvistag)
h1.SetTitle("Generated MC with rank1,Mbc_Bsig>5.27,-0.050<deltaE_Bsig<0.050 and abs(sin_phi)<1")

#Defining the width
h1.SetLineWidth(3)
h2.SetLineWidth(3)

#Defining the color
h1.SetLineColor(2)
h2.SetLineColor(4)

#Draw
%hipl h1
%hipl h2 s 

##plotting the legend
leg = TLegend(0.2,0.2,0.3,0.3)
#leg.AddEntry(h1,"Belle Data","l")
leg.AddEntry(h1,"Best sum of cosine angles","l")
#leg.AddEntry(h2,"Generated MC","l")
leg.AddEntry(h2,"cos(PBvistag,PBsig)+cos(PBtag,PBvistag)","l")
leg.Draw()
