#Importing the root
import ROOT
from ROOT import gROOT
from ROOT import TCanvas, TPad, TFile, TPaveLabel, TPaveText, THStack
from ROOT import TLegend
##Opening the signal file
#fs = TFile("incl_1M_with_mva_cuts.root")
fs = TFile("belle_data_all_exp_new_var.root")
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
%cut deltaE_sig_cut1 deltaE_Bsig>-0.15
%cut deltaE_sig_cut2 deltaE_Bsig<0.050
#%cut all_sig_side_cut Ycut&&Mbc_sig_cut&&deltaE_sig_cut1&&deltaE_sig_cut2
%cut all_sig_side_cut Mbc_sig_cut&&deltaE_sig_cut1&&deltaE_sig_cut2
%cut add_cut sin_cut

#Defining the histograms for best solutions
%1d h1_pdg 100 -1 3
%1d h2_reco 100 -1 3
#%1d cos_pBsig_soln2 100 -1.2 1.2

#Best solution plot preperation
%ntpl sig sin_phi Ycut&&Mbc_sig_cut&&deltaE_sig_cut1&&deltaE_sig_cut2 h1_pdg
%ntpl sig sin_phi_reco_jpsi_mass Ycut&&Mbc_sig_cut&&deltaE_sig_cut1&&deltaE_sig_cut2 h2_reco

#Setting the title  , and Mbc_Bsig>5.27
h2_reco.SetTitle("Sin_phi with rank 1,-0.15<deltaE_Bsig<0.050 and Mbc_Bsig>5.27")

#Defining the width
h1_pdg.SetLineWidth(3)
h2_reco.SetLineWidth(3)

#Defining the color
h1_pdg.SetLineColor(2)
h2_reco.SetLineColor(4)

#Draw
%hipl h2_reco
%hipl h1_pdg s 

##plotting the legend
leg = TLegend(0.2,0.2,0.3,0.3)
leg.AddEntry(h1_pdg,"PDG m_J/Psi","l")
leg.AddEntry(h2_reco,"Reco. m_J/Psi","l")
leg.Draw()
