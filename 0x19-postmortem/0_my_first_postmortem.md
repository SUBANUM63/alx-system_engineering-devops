# 1.Postmortem: API Service Downtime Incident
## Issue Summary:
### Duration of the Outage:
•	Start: June 14, 2024, 1:00 PM GMT+01:00
•	End: June 14, 2024, 2:45 PM GMT+01:00
### Impact:
•	Our primary API service was down, affecting approximately 60% of our users.
•	Users experienced failed requests and slow responses.
•	Affected critical functionalities of our service such as user authentication and data retrieval.
### Root Cause:
•	The root cause of the outage was an unexpected memory leak in the API service due to a recent update in the third-party library used for handling JSON requests.
________________________________________
#### Timeline:
•	1:00 PM: Monitoring alert triggered due to a significant increase in response times and failed requests.
•	1:05 PM: Engineers began initial investigation, checking server health and network issues.
•	1:15 PM: Confirmed no issues with server hardware or network. Started reviewing recent deployments.
•	1:25 PM: Focus shifted to the application layer. Logs showed increasing memory usage and failed API calls.
•	1:35 PM: Misleading assumption: Issue was related to database latency. Began optimizing database queries.
•	1:50 PM: Database optimizations had no effect. Escalated to the senior development team.
•	2:00 PM: Detailed log analysis revealed memory leak in the JSON handling library.
•	2:15 PM: Rolled back to previous stable version of the library.
•	2:30 PM: Restarted API services with the rolled-back library.
•	2:45 PM: Services fully restored, and users were able to access the API normally.
________________________________________
## Root Cause and Resolution:
### Root Cause:
•	The issue stemmed from a memory leak introduced by a recent update to a third-party JSON handling library. This update caused the API service to consume excessive memory, leading to crashes and unresponsiveness.
### Resolution:
•	The resolution involved rolling back the third-party library to the previous stable version. This stopped the memory leak and restored the API service. A detailed review of the library's update was scheduled to understand the specific changes that caused the issue.
________________________________________
## Corrective and Preventative Measures:

## Areas for Improvement:
### 1.Improve Testing:
o	Develop and integrate comprehensive tests for third-party library updates.
o	Include memory usage tests in the CI/CD pipeline.
### 2.Enhance Monitoring:
o	Add detailed memory usage metrics to the monitoring dashboard.
o	Set up alerts for abnormal memory usage patterns.
### 3.Robust Rollback Process:
o	Document the rollback procedures clearly.
o	Ensure all engineers are trained in executing quick rollbacks.
### 4.Review and Audit Third-Party Libraries:
o	Conduct a thorough review of all third-party libraries used.
o	Audit for potential issues and maintain a log of updates and their impacts.
### 5.User Communication Plan:
o	Develop a communication plan for informing users during outages.
o	Ensure timely updates to users on the status and resolution of issues.
## Tasks to Address the Issue:
### 1.Improve Testing:
o	Develop and integrate comprehensive tests for third-party library updates.
o	Include memory usage tests in the CI/CD pipeline.
### 2.Enhance Monitoring:
o	Add detailed memory usage metrics to the monitoring dashboard.
o	Set up alerts for abnormal memory usage patterns.
### 3.Robust Rollback Process:
o	Document the rollback procedures clearly.
o	Ensure all engineers are trained in executing quick rollbacks.
### 4.Review and Audit Third-Party Libraries:
o	Conduct a thorough review of all third-party libraries used.
o	Audit for potential issues and maintain a log of updates and their impacts.
### 5.User Communication Plan:
o	Develop a communication plan for informing users during outages.
o	Ensure timely updates to users on the status and resolution of issues.
________________________________________
## Conclusion:
This incident highlighted the importance of rigorous testing and monitoring, especially when updating third-party libraries. By implementing the corrective measures outlined, we aim to prevent similar issues in the future and improve the reliability of our services. We apologize for the inconvenience caused and appreciate our users' patience and understanding.

