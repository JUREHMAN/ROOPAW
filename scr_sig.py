#Importing the root
import ROOT
from ROOT import gROOT
from ROOT import TCanvas, TPad, TFile, TPaveLabel, TPaveText, THStack
from ROOT import TLegend
##Opening the signal file
#fs = TFile("incl_1M_with_mva_cuts.root")
fs = TFile("incl_1M_with_mva_photon_cuts.root")
%get Allincltag sig

fs1 = TFile("incl_1M_with_pi_zero_and_photon_cuts_zero_point_six.root ")
%get Allincltag sig1

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
#cut m_Dcut m_D-1.86 > 0.015
%cut cos_cut abs(cos_pBtag_Dltag)<1
%cut sin_cut abs(sin_phi)<1
%cut Ycut Yincl_rank_all==1
%cut best_cut abs(best_soln)<2
%cut lep_cut  nLepton==2
%cut mkpi_cut m_Kpi>2
%cut without_nL_cut m_Dcut&&Ycut&&best_cut
%cut with_nL_cut Ycut&&cos_cut&&sin_cut

#Defining the histograms for best solutions
%1d Signal 100 1.7 2.1
%1d Signal1 100 1.7 2.1
#Best solution plot preperation
%ntpl sig m_D with_nL_cut Signal
%ntpl sig1 m_D with_nL_cut Signal1
#Setting the title
Signal.SetTitle("m_D")


#Defining the width
Signal.SetLineWidth(3)
Signal1.SetLineWidth(3)

#Defining the color
Signal.SetLineColor(2)
Signal1.SetLineColor(4)
'''
#Not working in case of hstack
#Must be used after Draw otherwise it will give the null pointer error
hs.GetYaxis().SetRangeUser(0,250)
'''
#Draw
%hipl Signal
%hipl Signal1 s

##plotting the legend
leg = TLegend(0.2,0.2,0.3,0.3)
leg.AddEntry(Signal,"MVA cuts","l")
leg.AddEntry(Signal1,"Angular cuts","l")
leg.Draw()
