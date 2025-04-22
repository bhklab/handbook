# Offboarding Policy

Thank you for your time in the lab. To ensure a smooth transition and back up of your work, please follow the policy detailed below.
This policy applies to all individuals leaving BHK lab’s employ. It is meant to ensure that all staff who leave the employ of BHK lab ensure that all relevant intellectual and physical assets purchased with BHK lab funds remain in BHK lab. 

## Offboarding Meetings
Individuals under the employ of BHK lab who either received or provided a notice of termination shall abide by the following offboarding processes. The process shall include the following meetings: 

1. **Offboarding Initialization** - at least two (2) weeks prior to the last official working day

2. **Exit Interview** - a final meeting on the day prior to the employee's last official working day or based on availability

### Offboarding Initialization
An assigned lab staff member will contact the employee to set this meeting. This meeting will be use to summarize the off-boarding requirements.

- A folder will be shared with the employee to add documents discussed during the initial meeting. _This includes but is not restricted to a detailed back up of project details such as links to code, data folders and documentation._
- The [Lab Off-boarding Information template](https://docs.google.com/document/d/1KhnDPSIPqvjw7__1ACFVlBg7tS21bKxaR5AdPV6voUs/edit?tab=t.0#heading=h.j2hjmkdukzsc) will be shared with the employee. Please make a copy of this document in your offboarding report folder.
- The [Exit Interview Form](https://docs.google.com/forms/d/e/1FAIpQLSdnpTBRTcUmjQ0cnfP9MrN455Oy7tnW1JyRA4cgarvCs56pmQ/viewform?usp=sf_link) will be shared with the employee. This should be completed just prior to the exit interview.

    !!! warning
        If you expect continued work with the lab for a publication or similar activity, permissions to any of the lab services MUST be requested and marked in this Exit Interview form.

### Exit Interview
This meeting will be used to ensure all work items have been appropriately turned over and an exit interview will be conducted.

The final documents will be reviewed for completeness and accuracy by the lab member taking over the project or mentor (students). The members will identify any missing items, or items that require clarification by the employee. The terminated employee will develop a progress plan to address any issues that arise in this meeting.

---

## Offboarding Intellectual Assets

### Offboarding Report
Members leaving the lab will prepare a single digital parent folder containing all ongoing and completed project work. This folder shall be renamed to the first and last name of the employee leaving BHK lab. The parent folder's contents shall contain: 

1. The Lab Off-boarding Information document listing the following information:
        
    - [ ] The name and last date of employment of the employee;
    - [ ] All ongoing and completed projects that the terminated employee has worked on;
    - [ ] Links to the location of all items saved to Github organized by project;
    - [ ] Links to the location of all items saved to HPC4Health (H4H) organized by project, with all items saved to H4H adhering to the [H4H Data Management Plan](https://bhklab.github.io/HPC4Health/organizing_projects/data_management_plan/);
    - [ ] Details about data ownership for each project and name of the lab personnel in charge who takes over your project. All ownership should be transferred to this person-in-charge.

2. If applicable to individual projects, a single readme file that includes the following:

    - [ ] Data download sources;
    - [ ] Comments on data curation or any notable challenges;
    - [ ] Any other relevant information.

3. Any other relevant documents that are not caputred in (1) or (2).


This prepared folder will be shared by the terminated member with the assigned lab staff member, in addition to at least one (1) topic expert involved in each project included in the prepared folder. For short-term interns or volunteers, the parent folder can be shared with respective mentor(s). On receipt of the folder, each recipient shall confirm with the terminated employee the folder’s contents, including clarification for the contents and location of any items not included in the folder. 

**Link this document in your final SOW.**

!!! note
    All files related to your project that are linked in the above documents should be present in your BHKLab Google Drive account and shared with <bhklab-admin@googlegroups.com> and/or <bhklab-members@googlegroups.com> with **edit** access. The same applies for any relevant work documents. This is to ensure uninterrupted access without permission issues later.


### BHKLab Google Drive
To ensure continued access to all lab work related documents, we ask that the employee:

1. Upload all lab work related documents to your BHKLab Google Drive account. This includes any project related documents, presentations, etc. on your local machine. 

    !!! warning
        This should not include code or internal datasets. Please store these in the appropriate locations (e.g. GitHub, H4H, etc.).

1. Grant **edit** access to **all contents** of your BHKLab Google Drive to <bhklab-admin@googlegroups.com>. This can be done from the top level of the drive by selecting all contents and clicking the share button.

1. Change the password to their BHKLab Gmail account and share this with the lab coordinator.

If there are private documents you wish to keep private, please move these to your personal storage. 


### GitHub
#### Project Repositories
1. [Transfer any project repositories](https://docs.github.com/en/repositories/creating-and-managing-repositories/transferring-a-repository#transferring-a-repository-owned-by-your-personal-account) from your personal GitHub account to the BHKLab GitHub organization(https://github.com/bhklab).
2. Include a `README` describing the project and any project documentation explaining how to run the code and/or reproduce the results.

#### Open Pull Requests / Branches
1. If you have any open pull requests or working branches on any BHKLab project repositories, push the latest local commit you have. 
    1. If the branch does not already have an open pull request, create a new pull request.
1. Leave a comment on the PR describing what stage the branch is at and what next steps need to be taken.
1. Assign the PR to the repo owner, whoever is taking over the project, or your mentor.


### Project Data
For any project data listed in your Offboarding Report, please ensure that:

1. ALL data paths are included (e.g. srcdata, rawdata, procdata, should all be listed **separtely**).
1. Indicate for each dataset if it is required to replicate the project. This will help us determine if we can keep the data or if it needs to be removed.
1. Ensure that group access is enabled for all data. Run the following command for the dataset directory:

    ```bash
    chmod -R 775 <DIRECTORY_PATH>
    ```
    You can confirm that the data is accessible by running the following command:
    ```bash
    ls -l 
    total 2
    drwxrwxr-x  2 <USERNAME> <USERNAME> 4096 Jan  1 00:00 <DIRECTORY_PATH>
    ```

---

## Physical Assets Purchased by BHKLab
*Please ensure you return the assets to the lab coordinator in person.*

If an employee wishes to have possession of any BHK Lab asset purchased with operating funds and/or research funds, they may request from the employer permission to purchase such asset at fair market value.  The employer will determine if it is in the best interests of BHK Lab to sell the asset.

If the employer agrees to sell the asset, the employer shall determine fair market value through processes deemed appropriate by the employer. 

---

## On Your Last Day

On your official last day, please ensure that you return your Photo ID card and access card to the PMCRT Security office, located on the first floor of the MARS Discovery District.

---

## Letters of Recommendation
If an employee requires a letter of recommendation, s/he can send an email to Dr. Benjamin Haibe-Kains (<benjamin.haibe-kains@uhn.ca>) from their non-UHN email with mentors or other topic experts (optional) in cc. If the letter is required in the future, this email chain can be used. Please make sure the purpose of the letter is specified in your email. This is particularly relevant for short term students.


## Consequences for Non-Compliance
An individual whose employment with BHK Lab ends but who does not return BHK Lab assets in accordance with this policy may be subject to collection agency pursuit and/or legal action. Letters of recommendation or any similar styled letters will not be made out to any employee who fails to return lab assets in compliance with the stated offboarding processes and procedures. 
