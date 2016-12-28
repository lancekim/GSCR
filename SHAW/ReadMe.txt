              INSTRUCTIONS FOR RUNNING THE SHAW MODEL (Version 2.3)


     Thank you for your interest in the SHAW Model.  I hope you find the model 
useful for your particular application.  This ReadMe.txt file will hopefully get 
you started in using the model.  It contains information on running the sample 
input files provided with the model and compiling the model for non-DOS 
applications.

     Files included with this distribution of The Simultaneous Heat and Water 
(SHAW) Model include: this "ReadMe.txt" file; an executable image of the SHAW 
model (SHAW23.EXE); an error interpreter file for the Lahey FORTRAN compiler, 
just in case the program crashes (Lf90.EER); user-interface software 
(MODel SHELL, i.e. MODSHELL.EXE; a sample input file for the user interface 
(TRIALMOD.MOD); five trial input files for a sample SHAW run (TRIAL.*); and 
two directories named "Code" and "Output".  The FORTRAN source file for the 
SHAW model is located in directory "Code"; output from the trial input files 
are located in the directory "Output".  

     The five sample input files for the model are:

     TRIAL.INP  --  input file containing list of input/output files
     TRIAL.WEA  --  input file containing weather data
     TRIAL.SIT  --  input file containing site characteristics
     TRIAL.MOI  --  input file containing soil moisture profiles
     TRIAL.TMP  --  input file containing soil temperature profiles

You can run the SHAW model with or without the user-interface software.  The 
user interface has restrictions (such as no options for solute transport and no 
provisions for changing plant characteristics during the simulation) that are 
somewhat limiting. If this is the case, you can use the interface to build the 
input files, then alter them as needed.

    To run the sample input data set without the user-interface software, 
either double-click on the SHAW23.exe file within Windows or execute SHAW23 from
the MS-DOS prompt.  Upon executing SHAW23, enter "TRIAL.INP" when prompted for 
the file containing the list of input/output files.  The trial simulation may 
take a few minutes depending on the system you are using.  (The trial data set 
includes snow, canopy, residue and solutes, so it is likely to run slower than 
most applications.)  The trial simulation will generate the following files:

     OUT.OUT      -- output file for general information
     TEMP.OUT     -- simulated soil temperature profiles
     MOIST.OUT    -- simulated soil water profiles
     ENERGY.OUT   -- summary of simulated energy balance at the surface
     WATER.OUT    -- simulated water balance summary
     FROST.OUT    -- simulated frost, thaw, and snow depths

For information on specifying other output files that may be generated or on 
putting together data sets for your own applications, you are referred to 
either the user-interface or the instructions entitled "Input for the SHAW Model 
(Version 2.3)".  For information on the the user-interface software, see the 
instructions entitled "SHAW Interface Documentation".


UPDATES AND NEWS

Watch the SHAW Home Page on the internet for updates and news on the SHAW model.
The address is: http://www.nwrc.ars.usda.gov/Models/SHAW.html.  If you do not 
have access to the internet, you may request this information at the address 
given at the end of this file.


RUN-TIME ERRORS

     If for some reason the SHAW model encounters an error, the program will
search for the file Lf90.EER to interpret the error and hopefully give the user
some clue as to what the problem is.  If you get a message that it cannot find
this file, make sure it is in a directory where it can be found at the time you 
run the model.


COMPILING THE MODEL

     If you wish to run the model on a system other than MS-DOS, you will 
probably need to compile the program on the particular system you plan to use.  
The computer code for the model uses standard Fortran 77 and should be 
transferrable to most any system.  


ASSISTANCE

     If you have questions concerning the model, encounter problems, or need
additional information, please contact:

     Gerald N. Flerchinger
     USDA - ARS
     800 Park Blvd, Suite 105
     Boise, Idaho  83712
     (208) 422-0716
     Email: gflerchi@nwrc.ars.usda.gov
