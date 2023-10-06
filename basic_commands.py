###Opening the roopaw
roopaw

###Opening the root file
f = TFile("charged_genericMC.root")

##Extracting the tree
     get treename var
     get incltag t

###PLotting the variable inside the tree
      var.Draw("variable_name")
      t.Draw("m_D")


###Defining the histogram
     1Dimension histogram name bins xmin xmax
     1d h1 50 1 3

##Defining the cut
     cut cut_name cut defintion
     cut mcut abs(m_D)<2.5

##Defining the histogram
     ntpl treenmae variable histogram
     ntpl t m_D mcut h1

##Defining the new variable
form newvar var1 + var2
 
##PLotting the histogram
hipl h1
hipl h2 s

###Resetting the commands
reset

### Defining the color
h2.SetLineColor(2)

####Tree name should be declared immediately after opening the file

##For creating zones and plotting on the same screen
zone 2 3

##Tlegend don't work

