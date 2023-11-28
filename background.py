#Importing the root
import ROOT
from ROOT import gROOT
from ROOT import TCanvas, TPad, TFile, TPaveLabel, TPaveText, THStack
from ROOT import TLegend
##Opening the signal file
#fs = TFile("incl_1M_with_pi_zero_and_photon_cuts_zero_point_six.root")
#get Allincltag sig

#Opening the charged file
f1=TFile('charged_three_streams_mva_cuts.root')

#Getting the required tree
%get Allincltag charg

#Opening the Mixed file
f2=TFile('mixed_three_streams_mva_cuts.root')

#Getting the required tree
%get Allincltag mix

#Opening the Charm file
f3=TFile('charm_three_streams_mva_cuts.root ')

#Getting the required tree
%get Allincltag chrm

#Opening the Charm file
f4=TFile('uds_three_streams_mva_cuts.root')

#Getting the required tree
%get Allincltag ud

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
%cut Ycut Yincl_rank_all==1
%cut best_cut abs(best_soln)<2
%cut lep_cut  nLepton==2
%cut mkpi_cut m_Kpi>2
%cut without_nL_cut m_Dcut&&Ycut&&best_cut
%cut with_nL_cut Ycut&&best_cut&&lep_cut&&mkpi_cut&&m_Dcut

#Defining the histograms for best solutions
#1d Signal 100 1.92 2.0
%1d charged 100 1.84 1.88
%1d mixed 100 1.84 1.88
%1d charm 100 1.84 1.88
%1d uds 100 1.84 1.88
#1d hs 100 1.92 2.0

#For stacked histograms
hs = THStack("hs","Hadronic mass of the ROE system for generic MC");

#Best solution plot preperation

#ntpl sig nK_L_sig best_solution_cut Signal
#ntpl sig m_D with_nL_cut Signal

#ntpl charged nK_L_sig best_solution_cut charged
%ntpl charg m_D with_nL_cut charged

#ntpl mixed nK_L_sig best_solution_cut mixed
%ntpl mix m_D with_nL_cut mixed

#ntpl charm nK_L_sig best_solution_cut Best_Solution_charm
%ntpl chrm m_D with_nL_cut charm

#ntpl uds nK_L_sig best_solution_cut Best_Solution_uds
%ntpl ud m_D with_nL_cut uds

charged.SetFillColor(4)
mixed.SetFillColor(6)
charm.SetFillColor(8)
uds.SetFillColor(12)

hs.Add(charged)
hs.Add(mixed)
hs.Add(charm)
hs.Add(uds)
hs.Draw()
'''
#Setting the title
#charged.SetTitle("cos(PBtag,Pvis) in the region [m_D-1.86 > 0.015] generic MC")
Signal.SetTitle("m_D in the region between D and D*[abs(m_D-1.96)<0.03] generic and sig MC")
'''

#Defining the width
charged.SetLineWidth(3)
mixed.SetLineWidth(3)
charm.SetLineWidth(3)
uds.SetLineWidth(3)

#Defining the color
#Signal.SetLineColor(2)
charged.SetLineColor(4)
mixed.SetLineColor(6)
charm.SetLineColor(8)
uds.SetLineColor(12)

#Not working in case of hstack
#Must be used after Draw otherwise it will give the null pointer error
hs.GetYaxis().SetRangeUser(0,250)
'''
#Draw
hipl Signal
hipl charged s
hipl mixed s
hipl charm s
hipl uds s
'''

##plotting the legend
leg = TLegend(0.2,0.2,0.3,0.3)
#leg.AddEntry(Signal,"Signal","l")
leg.AddEntry(charged,"Charged","l")
leg.AddEntry(mixed,"mixed","l")
leg.AddEntry(charm,"Charm","l")
leg.AddEntry(uds,"uds","l")
leg.Draw()
