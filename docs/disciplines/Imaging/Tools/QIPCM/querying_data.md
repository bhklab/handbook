# [Querying Data from the QIPCM PACS](#querying-data-from-the-qipcm-pacs)

Once you've been added to a project's delegation log, the team at QIPCM will grant you access to the data. At this time of this writing, QIPCM cannot directly upload the data to H4H for us, so you will need to use the tools below to query the data and then upload it to [HPC4Health](../../../../software_development/Remote_Development/High_Performance_Computing_for_Health/index.md).



There are three tools you will need to access the data:

1. [The QIPCM Toolbox](https://qpmdcv-wprweb01.uhn.ca) (requires UHN Login)
2. [MongoDB Compass](https://www.mongodb.com/products/tools/compass)
3. [Horos](https://horosproject.org/)


!!! note
    You need to be connected to UHN-wireless-corporate wifi or the UHN VPN to access the QIPCM Toolbox for this process.

## Horos Setup

Horos is where the data from QIPCM will be sent to on your local machine. You will need to install Horos on your local machine to access the data.

After you have downloaded, installed, and launched Horos, you will need to configure it to connect to QIPCM's database. Navigate to the Preferences menu (on a Mac, this is found in the Horos menu bar, then Settings...). You need to setup [Locations](#horos-locations-menu) and Listener(#horos-listener-menu) configurations.

![](img/horos_preference_menu.jpg){width=70%}

### [The Locations Menu](#horos-locations-menu)
Click the "Add new node" button to create a node for QIPCM data.

![Screenshot of the Horos Preferences: Locations menu](img/horos_locations_menu.jpg){width=70%}

Set the following values for the new node:

- Address: qipcm-pacs.uhn.ca
- AETitle: QIPCM_OCTANE
- Port: 11112
- Q&R: Check box / Yes
- Retrieve: C-MOVE
- Send: Uncheck box / No
- TLS: Uncheck box / No
- Name: QIPCM {Project or Dataset Name}

Make sure you have checked the lefthand box so the location is active.

### [The Listener Menu](#horos-listener-menu)
![Screenshot of the Horos Preferences: Listener menu](img/horos_listener_menu.jpg){width=70%}

From Listener menu, copy the values for:

- AETitle
- Port Number
- Address
- Host Name

and send these to the QIPCM team member setting up your access.

Ensure the "Activate DICOM listener when Horos is running" box is checked.

You can now close the Preferences window, but need to leave Horos open and running for the remainder of this process.

!!! note
    Horos needs to be open for the duration of the data transfer from the QIPCM PACS to your local machine.


## Querying the data with MongoDB Compass

Open MongoDB Compass

1. Connect to your project's database. This will have been setup for you by the QIPCM team.
2. Navigate to scrapeDb on left hand side panel and select the collection you want to query.
3. On the right side of the window, next to the page navigation arrow, there is a hamburger menu, curly braces, and a table icon. Click the table icon to view the data in a table.
4. At this point, you may query a subset of the data (e.g. by modality, patient ID, etc.) or you may export the entire collection.
5. Once you have the data you want, click the EXPORT DATA button just above the table. Either export the query results or the full collection depending on step 4.
6. In the popup Export menu, under Fields to export, choose "Select fields in table". Then click "Next".
7. In the next window, select the following fields:

    - PatientID
    - Modality
    - SeriesInstanceUid
    - StudyInstanceUid
    then click "Next".

8. Select CSV as the Export File Type, then click "Export". Select where in your local file system you want to save the file and click "Save".






