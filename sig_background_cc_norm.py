#Importing the root
import ROOT
from ROOT import gROOT
from ROOT import TCanvas, TPad, TFile, TPaveLabel, TPaveText, THStack
from ROOT import TLegend
##Opening the belle data file
fs = TFile("belle_data_all_exp.root")
%get inclall sig

#Opening the charged file
f1=TFile('charged_three_streams_control_channel.root')

#Getting the required tree
%get inclall charg

#Opening the Mixed file
f2=TFile('mixed_three_streams_control_channel.root')

#Getting the required tree
%get inclall mix

#Opening the Charm file
f3=TFile('charm_three_streams_control_channel.root')

#Getting the required tree
%get inclall chrm

#Opening the Charm file
f4=TFile('uds_three_streams_control_channel.root')

#Getting the required tree
%get inclall ud

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
%cut less_m_D m_D<1.86
%cut greater_m_D m_D>2.006
%cut Ycut Yincl_rank_all==1
%cut best_cut abs(best_soln)<2
%cut lep_cut  nLepton==2
%cut mkpi_cut m_Kpi>2
%cut cos_cut abs(cos_pBtag_Dltag)<1
%cut sin_cut abs(sin_phi)<1
%cut Mbc_sig_cut Mbc_Bsig>5.27
%cut deltaE_sig_cut1 deltaE_Bsig>-0.050
%cut deltaE_sig_cut2 deltaE_Bsig<0.050

%cut without_nL_cut m_Dcut&&Ycut&&best_cut
#%cut with_nL_cut Ycut&&cos_cut&&sin_cut&&m_Dcut&&lep_cut&&mkpi_cut&&m_Dcut
%cut all_sig_Side_cut Mbc_sig_cut&&deltaE_sig_cut1&&deltaE_sig_cut2&&Ycut

#Defining the histograms for best solutions
%1d Signal 100 -2.2 2.2
%1d charged 100 -2.2 2.2
%1d mixed 100 -2.2 2.2
%1d charm 100 -2.2 2.2
%1d uds 100 -2.2 2.2

#ntpl sig nK_L_sig best_solution_cut Signal
%ntpl sig best_soln all_sig_Side_cut Signal

#ntpl charged nK_L_sig best_solution_cut charged
%ntpl charg best_soln all_sig_Side_cut charged

#ntpl mixed nK_L_sig best_solution_cut mixed
%ntpl mix best_soln all_sig_Side_cut mixed

#ntpl charm nK_L_sig best_solution_cut Best_Solution_charm
%ntpl chrm best_soln all_sig_Side_cut charm

#ntpl uds nK_L_sig best_solution_cut Best_Solution_uds
%ntpl ud best_soln all_sig_Side_cut uds

#Setting the title
#charged.SetTitle("m_hadROE cos(PBtag,Pvis) in the region [m_D-1.86 > 0.015] generic MC")
Signal.GetXaxis().SetTitle("(cos#theta_{1 }/cos#theta_{2}) + cos#theta_{tag}")
#Signal.GetYaxis().SetTitle("candidates/ (0.01)")
Signal.SetTitle("Best case ((cos#theta_{1 }/cos#theta_{2}) + cos#theta_{tag}) (closer to zero)")

#Normalizing the generic MC
'''
######Normalizing to one time signal
charged.Scale(1.0 / Signal.Integral(),"width");
mixed.Scale(1.0 / Signal.Integral(),"width");
charm.Scale(1.0 / Signal.Integral(),"width");
uds.Scale(1.0 / Signal.Integral(),"width");
'''

######Normalizing to three times the signal
charged.Scale(0.33 * (1.0 / Signal.Integral()),"width");
mixed.Scale(0.33 * (1.0 / Signal.Integral()),"width");
charm.Scale(0.33 * (1.0 / Signal.Integral()),"width");
uds.Scale(0.33 * (1.0 / Signal.Integral()),"width");


#Defining the width
Signal.SetLineWidth(3)
charged.SetLineWidth(3)
mixed.SetLineWidth(3)
charm.SetLineWidth(3)
uds.SetLineWidth(3)

#Defining the color
Signal.SetLineColor(2)
charged.SetLineColor(4)
mixed.SetLineColor(6)
charm.SetLineColor(8)
uds.SetLineColor(12)

'''
##Setting zero statistics
Signal.SetStats(0)
charged.SetStats(0)
mixed.SetStats(0)
charm.SetStats(0)
uds.SetStats(0)
'''

#Draw
%hipl Signal e
%hipl charged s
#%hipl Signal e s
%hipl mixed s
%hipl charm s
%hipl uds s

##plotting the legend
leg = TLegend(0.2,0.2,0.3,0.3)
leg.AddEntry(Signal,"Signal shape (Belle Data)","l")
leg.AddEntry(charged,"B^{+}B^{-}","l")
leg.AddEntry(mixed,"B^{0}#bar{B^{0}}","l")
leg.AddEntry(charm,"e^{+}e^{-} #rightarrow c#bar{c}","l")
leg.AddEntry(uds,"e^{+}e^{-} #rightarrow u#bar{u},d#bar{d},s#bar{s}","l")
leg.Draw()
