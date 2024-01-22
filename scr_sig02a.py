#Importing the root
import ROOT
from ROOT import gROOT
from ROOT import TCanvas, TPad, TFile, TPaveLabel, TPaveText, THStack
from ROOT import TLegend
##Opening the signal file
#fs = TFile("incl_1M_with_mva_cuts.root")
fs = TFile("belle_data_all_exp.root")
%get inclall sig

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
%cut all_sig_side_cut Mbc_sig_cut&&deltaE_sig_cut1&&deltaE_sig_cut2
%cut add_cut sin_cut

#Defining the histograms for best solutions
%1d h1 100 0 4
#%1d cos_pBsig_soln2 100 -1.2 1.2

#Best solution plot preperation
%ntpl sig sin_phi:deltaE_Bsig Ycut&&Mbc_sig_cut h1
#%ntpl sig cos_theta_sol2_Bsig_mom all_sig_side_cut cos_pBsig_soln2  -0.15<deltaE_Bsig<0.050

#Setting the title abs(sin_phi)<1
h1.SetTitle("sin_phi:deltaE_Bsig with rank 1, and Mbc_Bsig>5.27")

#Defining the width
h1.SetLineWidth(3)
#cos_pBsig_soln2.SetLineWidth(3)
h1.GetYaxis().SetRangeUser(-3,3)
h1.GetXaxis().SetRangeUser(-2,2)

#Defining the color
h1.SetLineColor(2)
#cos_pBsig_soln2.SetLineColor(4)

#Draw
%hipl h1
#%hipl cos_pBsig_soln2 s 

##plotting the legend
leg = TLegend(0.2,0.2,0.3,0.3)
leg.AddEntry(h1,"Belle data","l")
#leg.AddEntry(cos_pBsig_soln2,"Cosine of the angle between Bsig momentum and the solution 2","l")
leg.Draw()
