# CI.md

## GitHub actions

1. Keep your Actions minimal
2. Don’t install dependencies unnecessarily
3. Never hardcode secrets
4. Limit environment variables to the narrowest possible scope
5. Use self-hosted runners, except with public repositories
6. Use GitHub marketplace
7. Handle uncerified actions (block / fork / case by case)

## Jenkins

1. Keep Jenkins Secure
2. Always Backup The “JENKINS_HOME” Directory
3. Setup A Different Job/Project For Each Maintenance Or Development Branch
4. Prevent Resource Collisions In Jobs That Are Running In Parallel
5. Use “File Fingerprinting” To Manage Dependencies
6. Avoid Complicated Groovy Codesode In Pipelines
7. Build A Scalable Jenkins Pipeline
8. Manage Declarative Syntax/Declarative Pipelines
9. Maintain Higher Test Code Coverage & Run Unit Tests As Part Of Your Pipeline
10. Monitor Your CI/CD Pipeline
11. Avoid calls to Jenkins.getInstance
12. Do not override built-in Pipeline steps
13. Avoiding large global variable declaration files
14. Ensure Persisted Variables Are Serializable
15. Reducing repetition of similar Pipeline steps
16. Integrate tightly with your issue tracking system, like JIRA or bugzilla, to reduce the need for maintaining a Change Log
17. Set up Jenkins on the partition that has the most free disk-space
18. Avoid scheduling all jobs to start at the same time
19. Set up email notifications mapping to ALL developers in the project, so that everyone on the team has his pulse on the project's current status
20. Take steps to ensure failures are reported as soon as possible.
21. Write jobs for your maintenance tasks, such as cleanup operations to avoid full disk problems.
22. Tag, label, or baseline the codebase after the successful build.
