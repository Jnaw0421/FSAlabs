#!/usr/bin/env python3

#total questions = 64
#-----------------------
def main(): 
    guesses= []
    correct_guesses = 0
    question_num = 1


    for key in questions:
        print()
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input()
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_anwser(questions.get(key),guess)
        question_num += 1
    display_score(correct_guesses, guesses)
#-----------------------
def check_anwser(answer, guess):
    if answer == guess:
        print('Correct')
        return 1
    else: 
        print('Wrong')
        #print(review)
        return 0
#-----------------------
def display_score(correct_guesses, guesses):
    print()
    print("Results")
    print()

    '''
    print('Anwsers: ', end='')
    for i in questions:
        print(questions.get(i), end=' ')
        print()

    print('Guesses: ', end='')
    for i in Guesses:
        print(i, end=' ')
        print()
    '''
    score = (correct_guesses/len(questions))*100
    print('Your score is: '+str(score)+'%')
    print("Heres a document for review: https://docs.google.com/document/d/1MDB93my4gUsPRsccq5aQsW4w9OWgKGQ8Gx8YeMOJw8Q/edit?usp=sharing")
#-----------------------
def play_again(): 
    response = input("Do you want to play again? (Yes or No):")
    response = response.upper()

    if response == 'Yes':
        return True
    else: 
        return False
        

questions = {
    "A Cloud Practitioner is developing a new application and wishes to integrate features of AWS services directly into the application. \n Which of the following is the BEST tool for this purpose?: " : "B",
    "Which tasks require the use of the AWS account root user? (Select TWO.): " : "A, E", 
    "Which of the following AWS features or services can be used to provide root storage volumes for Amazon EC2 instances?: " : "D",
    "Which of the following deployments involves the reliability pillar of the AWS Well-Architected Framework?:" : "C",
    "A company uses Amazon EC2 instances to run applications that are dedicated to different departments. The company needs to break out the costs of these applications and allocate them to the relevant department. The EC2 instances run in a single VPC.\n How can the company achieve these requirements?" : "B",
    "A large company is interested in avoiding long-term contracts and moving from fixed costs to variable costs.\nWhat is the value proposition of AWS for this company?" : "A",
    "Which tasks can a user complete using the AWS Cost Management tools? (Select TWO.)" : "A, D",
    "Which type of credential should a Cloud Practitioner use for programmatic access to AWS resources from the AWS CLI/API?" : "A",
    "A user needs to identify underutilized Amazon EC2 instances to reduce costs.\nWhich AWS service or feature will meet this requirement?" : "C",
    "What is one method of protecting against distributed denial of service (DDoS) attacks in the AWS Cloud?" : "D",
    "A company is designing a new a service that must align with the operational excellence pillar of the AWS Well-Architected Framework.\nWhich design principles should the company follow? (Select TWO.)" : "B, C",
    "A company is migrating a monolithic application that does not scale well into the cloud and refactoring it into a microservices architecture.\nWhich best practice of the AWS Well-Architected Framework does this plan relate to?" : "D",
    "Which AWS Cloud service provides recommendations on how to optimize performance for AWS services?" : "C",
    "A company plans to deploy a relational database on AWS. The IT department will perform database administration. Which service should the company use?" : "C",
    "Which of the following are valid benefits of using the AWS Cloud? (Select TWO.)" : "A, B",
    "For what purpose would a Cloud Practitioner access AWS Artifact?" : "D",
    "A company is deploying an application in the AWS Cloud. How can they secure the application? (Select TWO.)" : "B, C",
    "A company is deploying a new workload and software licensing requirements dictate that the workload must be run on a specific, physical server. \nWhich Amazon EC2 instance deployment option should be used?" : "A",
    "When running applications in the AWS Cloud, which common tasks can AWS manage on behalf of their customers? (Select TWO.)" : "B, C",
    "What advantages does a database administrator obtain by using the Amazon Relational Database Service (RDS)?" : "A",
    "Which of the following statements best describes the concept of agility in relation to cloud computing on AWS? (Select TWO.)" : "B, C",
    "A company needs to publish messages to a thousands of subscribers simultaneously using a push mechanism.\nWhich AWS service should the company use?" : "D",
    "Which of the following is a sole responsibility of AWS?" : "A",
    "Which AWS services can a company use to gather information about activity in their AWS account? (Select TWO.)" : "C, E",
    "A company is deploying a MySQL database on AWS. The database must easily scale and have automatic backup enabled.\nWhich AWS service should the company use?" : "D",
    "What are AWS Identity and Access Management (IAM) access keys used for?" : 'B',
    "Which AWS service or feature can assist with protecting a website that is hosted outside of AWS?" : "C",
    "A company is planning to deploy an application with a relational database on AWS. The application layer requires access to the database instances operating system in order to run scripts.\nThe company prefer to keep management overhead to a minimum. Which deployment should be used for the database?" : "C",
    "A company has many underutilized compute resources on-premises. Which AWS Cloud feature will help resolve this issue?" : "A",
    "A company is deploying a new web application in a single AWS Region that will be used by users globally.\nWhich AWS services will assist with lowering latency and improving transfer speeds for the global users? (Select TWO.)" : "B, C", 
    "A Cloud Practitioner requires point-in-time recovery (PITR) for an Amazon DynamoDB table. Who is responsible for configuring and performing backups?" : "B",
    "Customers using AWS services must patch operating systems on which of the following services?" : "A",
    "Which of the following represents a value proposition for using the AWS Cloud?" : "B",
    "An Amazon Virtual Private Cloud (VPC) can include multiple:" : "B",
    "According to the AWS shared responsibility model, which of the following is a responsibility of AWS?" : "D",
    "A company has multiple AWS accounts and is using AWS Organizations with consolidated billing. Which advantages will they benefit from? (Select TWO.)" : "B, D",
    "AWS are able to continually reduce their pricing due to:" : "B",
    "A company is planning to move a number of legacy applications to the AWS Cloud. The solution must be cost-effective. Which approach should the company take?" : "D",
    "A company is deploying an application on Amazon EC2 that requires low-latency access to application components in an on-premises data center. Which AWS service or resource can the company use to extend their existing VPC to the on-premises data center?" : "B",
    "A company runs a batch job on an Amazon EC2 instance and it takes 6 hours to complete. The workload is expected to double in volume each month with a proportional increase in processing time." : "A",
    "Which design principles are enabled by the AWS Cloud to improve the operation of workloads? (Select TWO.)" : "A, E",
    "How much data can a company store in the Amazon S3 service?" : "A",
    "A customer needs to determine Total Cost of Ownership (TCO) for a workload that requires physical isolation. Which hosting model should be accounted for?" : "B",
    "An individual IAM user must be granted access to an Amazon S3 bucket using a bucket policy. Which element in the S3 bucket policy should be updated to define the user account for which access will be granted?" : "B",
    "A user is planning to launch three EC2 instances behind a single Elastic Load Balancer. The deployment should be highly available. How should the user achieve this?" : "A",
    "How does the AWS cloud increase the speed and agility of execution for customers? (Select TWO.)" : "B, D",
    "Which of the following AWS services are compute services? (Select TWO.)" : "A, C",
    "An application uses a PostgreSQL database running on a single Amazon EC2 instance. A Cloud Practitioner has been asked to increase the availability of the database so there is automatic recovery in the case of a failure.\nWhich tasks can the Cloud Practitioner take to meet this requirement?" : "B",
    "What is the best practice for managing AWS IAM access keys?" : "B",
    "What can a Cloud Practitioner use to categorize and track AWS costs by project?" : "B",
    "Which resource should a new user on AWS use to get help with deploying popular technologies based on AWS best practices, including architecture and deployment instructions?" : "C",
    "A company plans to use reserved instances to get discounted pricing for Amazon EC2 instances. The company may need to change the EC2 instance type during the one year period.\nWhich instance purchasing option is the MOST cost-effective for this use case?" : "A",
    "A website has a global customer base and users have reported poor performance when connecting to the site.\nWhich AWS service will improve the customer experience by reducing latency?" : "D",
    "A Cloud Practitioner needs to monitor a new Amazon EC2 instances CPU and network utilization. Which AWS service should be used?" : "C",
    "A company is launching a new website which is expected to have highly variable levels of traffic. The website will run on Amazon EC2 and must be highly available. \n What is the MOST cost-effective approach?" : "D",
    "A company must provide access to AWS resources for their employees. Which security practices should they follow? (Select TWO.)" : "B, C",
    "A Cloud Practitioner needs a tool that can assist with viewing and managing AWS costs and usage over time. Which tool should the Cloud Practitioner use?" : "A",
    "Which benefits can a company gain by deploying a relational database on Amazon RDS instead of Amazon EC2? (Select TWO.)" : "A, C",
    "Which AWS service can a company use to discover and protect sensitive data that is stored in Amazon S3 buckets." : "B",
    "Which AWS service provides a managed software version control system?" : "B",
    "Which AWS service can a team use to deploy infrastructure on AWS using familiar programming languages?" : "D",
    "A Cloud Practitioner anticipates an increase in application traffic at a future date and time when a sales event will take place. How can the Cloud Practitioner configure Amazon EC2 Auto Scaling to ensure the right number of Amazon EC2 instances are available ahead of the event?" : "A",
    "Which of the following can an AWS customer use to launch a new ElastiCache cluster? (Select TWO.)" : "A, B",
    "Which AWS feature can be used to launch a pre-configured Amazon Elastic Compute Cloud (EC2) instance?" : "A",
    "Which of the following will help a user determine if they need to request an Amazon EC2 service limit increase?" : "C",


}
options = [
        ['A. AWS CodePipeline', 'B. AWS Software Development Kit', 'C. AWS CodeDeploy', 'D. AWS Command Line Interface (CLI)'], 
        ['A. Changing AWS Support plans.', 'B. Changing payment currency', 'C. Enabling encryption for S3.', 'D. Viewing AWS CloudTrail logs.', 'E. Changing the account name.'],
        ['A. Amazon Simple Storage Service (S3)', 'B. Amazon Machine Image', 'C. Amazon Elastic File System (EFS)', 'D. Amazon Elastic Block Store (EBS)'],
        ['A. Use CloudFormation to deploy infrastructure', 'B Attach a WebACL to a CloudFront distribution', 'C. Amazon RDS Multi-AZ deployment', 'D. Amazon EBS provisioned IOPS volume'],
        ['A.Add additional Amazon VPCs and launch each application in a separate VPC.', 'B. Create tags by department on the instances and then run a cost allocation report.', 'C. Enable billing alerts through Amazon CloudWatch and Amazon SNS.', 'D. Enable billing access for IAM users and view the costs in Cost Explorer.'],
        ['A. Pay-as-you-go pricing', 'B. Automated cost optimization', 'C. Volume pricing discounts', 'D. Economies of scale'], 
        ['A. Create budgets and receive notifications if current or forecasted usage exceeds the budgets.', 'B. Launch either EC2 Spot instances or On-Demand instances based on the current pricing.', 'C. Delete all of your AWS resources with a single click.', 'D. Automatically terminate AWS resources if budget thresholds are exceeded.', 'E. Move data stored in Amazon S3 Standard to an archiving storage class to reduce cost.'],
        ['A. Access keys', 'B. SSL/TLS certificate', 'C. User name and password', 'D. SSH public keys'],
        ['A. AWS Health Dashboard', 'B. AWS Cost Explorer', 'C. AWS Trusted Advisor', 'D. AWS CodeBuild'],
        ['A. Use Amazon CloudWatch monitoring.', 'B. Monitor the AWS Health Dashboard.', 'C. Enable AWS CloudTrail logging.', 'D. Configure a firewall in front of resources.'],
        ['A. Perform manual operations.', 'B. Perform operations as code.', 'C. Anticipate failure.', 'D. Make large-scale changes.', 'E. Create static operational procedures.'],
        ['A. Manage change in automation.', 'B. Stop spending money on undifferentiated heavy lifting.',  'C. Use multiple solutions to improve performance.', 'D. Implement loosely coupled services.'],
        ['A. Amazon CloudWatch', 'B. Amazon Inspector', 'C. AWS Trusted Advisor', 'D. AWS CloudTrail'],
        ['A. Amazon RedShift', 'B. Amazon DynamoDB', 'C. Amazon EC2', 'D. Amazon ElastiCache'],
        ['A. Ability to go global quickly.', 'B. Fast provisioning of IT resources.', 'C. Outsource all operational risk.', 'D. Outsource all application development to AWS.', 'E. Total control over data center infrastructure.'],
        ['A. Access training materials for AWS services.', 'B. Create a security assessment report for AWS services.', 'C. Download configuration details for all AWS resources.', 'D. Gain access to AWS security and compliance documents.'],
        ['A. Enable monitoring by turning off encryption for data in transit.', 'B. Limit access privileges according to the principal of least privilege.', 'C. Enable encryption for the application data at rest.', 'D. Configure public access for the AWS services used by the application.', 'E. Provide full admin access to developer and operations staff.'],
        ['A. Dedicated Hosts', 'B. Reserved Instances', 'C. Dedicated Instances', 'D. Spot Instances'],
        ['A. Application security testing', 'B. Patching database software', 'C. Taking a backup of a database', 'D. Application source code auditing', 'E. Creating a database schema'],
        ['A. RDS simplifies relational database administration tasks.', 'B. RDS provides 99.99999999999% reliability and durability.', 'C. RDS databases automatically scale based on load.', 'D. RDS enables users to dynamically adjust CPU and RAM resources.'],
        ['A. The speed at which AWS rolls out new features.', 'B. The speed at which AWS resources can be created.', 'C. The ability to experiment quickly.', 'D. The ability to automatically scale capacity.', 'E. The elimination of wasted capacity.'],
        ['A. Amazon Simple Workflow Service (SWF)', 'B. AWS Step Functions', 'C. Amazon Simple Queue Service (Amazon SQS)', 'D. Amazon Simple Notification Service (Amazon SNS)'],
        ['A. Availability Zone management', 'B. Customer data access controls', 'C. Application deployment', 'D. Patch management'],
        ['A. Amazon CloudFront', 'B. AWS Trusted Advisor', 'C. AWS CloudTrail', 'D. Amazon Connect', 'E. Amazon CloudWatch'],
        ['A. Amazon DocumentDB', 'B. Amazon Athena', 'C. Amazon DynamoDB', 'D. Amazon Aurora'], 
        ['A. Logging in to the AWS Management Console.', 'B. Making programmatic calls to AWS from AWS APIs.', 'C. Ensuring the integrity of log files.', 'D. Enabling encryption in transit for web servers.'],
        ['A. Amazon EC2 security groups', 'B. Amazon VPC route tables', 'C. AWS Web Application Firewall (WAF)', 'D. Amazon VPC network ACLs'],
        ['A. Amazon DynamoDB', 'B. Amazon RDS', 'C. Amazon EC2', 'D. Amazon S3'],
        ['A. Elasticity', 'B. Global deployment', 'C. High availability', 'D. Fault tolerance'],
        ['A. AWS Direct Connect', 'B. Amazon CloudFront', 'C. AWS Transit Gateway', 'D. AWS Global Accelerator', 'E. AWS Snowcone'],
        ['A. AWS is responsible for both tasks.', 'B. The customer is responsible for configuring and AWS is responsible for performing backups.', 'C. AWS is responsible for configuring and the user is responsible for performing backups.', 'D. The customer is responsible for both tasks.'],
        ['A. Amazon EC2', 'B. AWS Fargate', 'C. AWS Lambda', 'D. Amazon DynamoDB'],
        ['A. AWS provides full access to their data centers.', 'B. It is not necessary to enter into long term contracts.', 'C. AWS is responsible for securing your applications.', 'D. Customers can request specialized hardware.'],
        ['A. Internet gateways.', 'B. Availability Zones.', 'C. Edge locations.', 'D. AWS Regions.'],
        ['A. Configuring network ACLs to block malicious attacks.', 'B. Updating security group rules to enable connectivity.', 'C. Patching software running on Amazon EC2 instances.', 'D. Updating the firmware on the underlying EC2 hosts.'],
        ['A. They will receive a fixed discount for all usage across accounts.', 'B. They may benefit from lower unit pricing for aggregated usage.', 'C. They will be automatically enrolled in a business support plan.', 'D. They will receive one bill for the accounts in the Organization.', 'E. The default service limits in all accounts will be increased.'],
        ['A. Pay-as-you go pricing.', 'B. Economies of scale.', 'C. Compute savings plans.', 'D. Elastic compute services.'],
        ['A. Use AWS Lambda to host the legacy applications in the cloud.', 'B. Migrate the applications to dedicated hosts on Amazon EC2.', 'C. Use an Amazon S3 static website to host the legacy application code.', 'D. Rehost the applications on Amazon EC2 instances that are right-sized.'],
        ['A. Amazon Workspaces', 'B. AWS Outposts', 'C. AWS Direct Connect', 'D. Amazon Connect'],
        ['A. Run the batch workload in parallel across multiple Amazon EC2 instances.', 'B. Change the Amazon EC2 volume type to a Provisioned IOPS SSD volume.', 'C. Run the batch job on a larger Amazon EC2 instance type with more CPU.', 'D. Run the application on a bare metal Amazon EC2 instance.'],
        ['A. Remove single points of failure', 'B. Customized hardware', 'C. Minimize platform design', 'D. Minimum viable product', 'E. Loose coupling'],
        ['A. Virtually unlimited', 'B. 100 TB', 'C. 1 PB', 'D. 100 PB'],
        ['A. Reserved Instances', 'B. Dedicated Hosts', 'C. Spot Instances', 'D. On-Demand Instances'],
        ['A. Resource', 'B. Principal', 'C. Action', 'D. Condition'],
        ['A. Launch the instances across multiple Availability Zones in a single AWS Region.', 'B. Launch the instances as EC2 Reserved Instances in the same AWS Region, but in different Availability Zones.', 'C. Launch the instances in multiple AWS Regions, and use Elastic IP addresses.', 'D. Launch the instances as EC2 Spot Instances in the same AWS Region and the same Availability Zone.'],
        ['A. Private connections to data centers', 'B. Scalable compute capacity', 'C. Secured data centers', 'D. Fast provisioning of resources', 'E. Lower cost of deployment'],
        ['A. AWS Elastic Beanstalk', 'B. AWS CloudTrail', 'C. AWS Batch', 'D. Amazon EFS', 'E. Amazon Inspector'],
        ['A. Set the DeleteOnTermination value to false for the EBS root volume.', 'B. Migrate the database to Amazon RDS and enable the Multi-AZ feature.', 'C. Configure an Elastic Load Balancer in front of the EC2 instance.', 'D. Configure EC2 Auto Recovery to move the instance to another Region.'],
        ['A. Never use access keys, always use IAM roles.', 'B. Customers should rotate access keys regularly.', 'C. AWS rotate access keys on a schedule.', 'D. There is no need to manage access keys.'],
        ['A. Consolidated billing', 'B. Cost Allocation Tags', 'C. Multiple accounts', 'D. AWS Trusted Advisor'],
        ['A. AWS Config', 'B. AWS Artifact', 'C. AWS Quick Starts', 'D. AWS CloudFormation'],
        ['A. Convertible Reserved Instances', 'B. Standard Reserved Instances', 'C. Regional Reserved Instances', 'D. Zonal Reserved Instances'],
        ['A. AWS Direct Connect', 'B. Amazon EC2 Auto Scaling', 'C. Amazon ElastiCache', 'D. Amazon CloudFront'],
        ['A. AWS CloudTrail', 'B. AWS Systems Manager', 'C. Amazon CloudWatch', 'D. Amazon Inspector'],
        ['A. Launch the website using an Amazon EC2 instance running on a dedicated host.', 'B. Determine the highest expected traffic and use an appropriate instance type.', 'C. Use the AWS CLI to launch and terminate Amazon EC2 instances to match demand.', 'D. Create an Amazon EC2 Auto Scaling group and configure an Elastic Load Balancer.'],
        ['A. Disable password policies and management console access.', 'B. Enable multi-factor authentication for users.', 'C. Create IAM policies based on least privilege principles.', 'D. Create IAM users in different AWS Regions.', 'E. Create IAM Roles and apply them to IAM groups.'],
        ['A. AWS Cost Explorer', 'B. AWS Budgets', 'C. Amazon Inspector', 'D. AWS Organizations'],
        ['A. Automated backups', 'B. Schema management', 'C. Software patching', 'D. Indexing of tables', 'E. Root access to OS'],
        ['A. AWS Policy Generator', 'B. Amazon Macie', 'C. Amazon GuardDuty', 'D, Amazon Detective'],
        ['A. Amazon CodeDeploy', 'B. AWS CodeCommit', 'C. AWS CodePipeline', 'D. AWS DataSync'],
        ['A. AWS CodeCommit', 'B. Amazon CodeGuru', 'C. AWS Config', 'D. AWS Cloud Development Kit (AWS CDK)'],
        ['A. Configure a scheduled scaling policy.', 'B. Configure a step scaling policy.', 'C. Configure predictive scaling.', 'D. Configure a target tracking scaling policy.'],
        ['A. AWS Management Console', 'B. AWS CloudFormation', 'C. AWS Data Pipeline', 'D. AWS Systems Manager', 'D. AWS Concierge'],
        ['A. Amazon Machine Image (AMI)', 'B. Amazon EC2 Systems Manager', 'C. Amazon AppStream 2.0', 'D. Amazon Elastic Block Store (EBS)'],
        ['A. Amazon RDS', 'B. AWS Cost Explorer', 'C. AWS Trusted Advisor', 'D. AWS Health Dashboard'],

]
review = {
        'Explanation : A software development kit (SDK) is a collection of software development tools in one installable package. AWS provide SDKs for various programming languages and these can be used for integrating the features of AWS services directly into an application.',
        'Explanation : Some tasks can only be performed by the root user of an AWS account. This includes changing the account name and changing AWS support plans. For more information view the AWS article referenced below.',
        'Explanation : The Amazon Elastic Block Store (EBS) provides block-based storage volumes for Amazon EC2 instances. Root volumes are where the operating system is installed and can be either EBS volumes or instance store volumes.',
        'Explanation : An Amazon Relational Database Service (RDS) deployment across multiple availability zones is a good example of using the reliability pillar of the AWS Well-Architected Framework. The specific design principle being followed here is “Automatically recover from failure”.',
        'Explanation : The company should create cost allocation tags that specify the department and assign them to resources. These tags must be activated so they are visible in the cost allocation report. Once this is done and a monthly cost allocation report has been configured it will be easy to monitor the costs for each department.',
        'Explanation : Pay-as-you-go pricing helps companies move away from fixed costs to variable costs in a model in which they only pay for what they actually use. There are no fixed term contracts with AWS so that requirement is also met.',
        'Explanation : The AWS Cost Management tools includes services, tools, and resources to organize and track cost and usage data, enhance control through consolidated billing and access permissions, enable better planning through budgeting and forecasts, and further lower costs with resources and pricing optimizations.',
        'Explanation : Access keys are long-term credentials for an IAM user or the AWS account root user. You can use access keys to sign programmatic requests to the AWS CLI or AWS API (directly or using the AWS SDK).',
        'Explanation : AWS Trusted Advisor offers a rich set of best practice checks and recommendations across five categories: cost optimization, security, fault tolerance, performance, and service limits. \n The Trusted Advisor “low utilization Amazon EC2 instances” check, checks the Amazon Elastic Compute Cloud (Amazon EC2) instances that were running at any time during the last 14 days and alerts you if the daily CPU utilization was 10% or less and network I/O was 5 MB or less on 4 or more days.',
        'Explanation : Some forms of DDoS mitigation are included automatically with AWS services. You can further improve your DDoS resilience by using an AWS architecture with specific services and by implementing additional best practices. Using a firewall with AWS resources is recommended to reduce the attack surface of your services which can mitigate some DDoS attacks.',
        'Explanation : AWS Well-Architected helps cloud architects build secure, high-performing, resilient, and efficient infrastructure for their applications and workloads. There are 5 pillars and under the operational excellence pillar the following best practices are recommended:',
        'Explanation : A microservices architecture will help ensure that each component of the application can scale independently and be updated independently. Loose coupling further assists as it places reduces the dependencies between systems and ensures that messages and data being passed between application components can be reliably and durably stored.',
        'Explanation : AWS Trusted Advisor can improve the performance of your service by checking your service limits, ensuring you take advantage of provisioned throughput, and monitoring for overutilized instances.',
        'Explanation : A self-managed relational database can be installed on Amazon EC2. When using this deployment you can choose the operating system and instance type that suits your needs and then install and manage any database software you require. The table below helps you to understand when to use different types of database deployment:',
        'Explanation : The ability to provision IT resources quickly and easily and also globally are valid benefits of using the AWS cloud. These are covered in AWS’ 6 advantages of cloud which include “Increase speed and agility” and “Go global in minutes”.',
        'Explanation : AWS Artifact is your go-to, central resource for compliance-related information that matters to you. It provides on-demand access to AWS’ security and compliance reports and select online agreements. Reports available in AWS Artifact include our Service Organization Control (SOC) reports, Payment Card Industry (PCI) reports, and certifications from accreditation bodies across geographies and compliance verticals that validate the implementation and operating effectiveness of AWS security controls.',
        'Explanation : In this scenario the company must apply best practice principals for securing their application. Enabling encryption for data at rest is definitely a good practice and data in transit should also be encrypted where possible as well. It is also a good practice to limit access privileges according to the principal of least privilege. This means limiting privileges to those required to perform a specific role.',
        'Explanation : An Amazon EC2 Dedicated Host is a physical server fully dedicated for your use, so you can help address corporate compliance requirements. Amazon EC2 Dedicated Hosts allow you to use your eligible software licenses from vendors such as Microsoft and Oracle on Amazon EC2, so that you get the flexibility and cost effectiveness of using your own licenses, but with the resiliency, simplicity and elasticity of AWS',
        'Explanation : With AWS managed services you can reduce your time spent performing common IT tasks. With services such as Amazon RDS, AWS will patch the database host operating system and database software and perform patch management activities.',
        'Explanation : Amazon RDS is a managed relational database service on which you can run several types of database software. The service is managed so this reduces the database administration tasks an administrator would normally undertake. The managed service includes hardware provisioning, database setup, patching and backups.',
        'Explanation : In a cloud computing environment, new IT resources are only a click away, which means that you reduce the time to make those resources available to your developers from weeks to just minutes. This results in a dramatic increase in agility for the organization, since the cost and time it takes to experiment and develop is significantly lower.',
        'Explanation : Amazon SNS is a publisher/subscriber notification service that uses a push mechanism to publish messages to multiple subscribers. Amazon SNS enables you to send messages or notifications directly to users with SMS text messages to over 200 countries, mobile push on Apple, Android, and other platforms or email (SMTP).',
        'Explanation : According to the shared responsibility model, AWS is responsible to the management of all AWS global infrastructure components including Regions, Availability Zones, Edge locations, Regional Edge Caches, and Local Zones.',
        'Explanation : Amazon CloudWatch is a performance monitoring service. AWS services send metrics about their utilization to CloudWatch which collects the metrics. Additionally, CloudWatch collects metrics about account activity such as billing information which can also be viewed.',
        'Explanation : Amazon Aurora is a relational database that is compatible with MySQL and PostgreSQL database engines. Aurora is extremely fast and scales up to 128 TB. You can also deploy replicas for read scaling within and across Regions. Aurora also offers automated backups.',
        'Explanation : Access keys are long-term credentials for an IAM user or the AWS account root user. You can use access keys to sign programmatic requests to the AWS CLI or AWS API (directly or using the AWS SDK).',
        'Explanation : AWS WAF can be used to protect on-premises resources if they are deployed behind an Application Load Balancer (ALB). In this scenario the on-premises website servers are added to a target group by IP address. The ALB has a WAF WebACL attached to it and distributes connections to the on-premises website.',
        'Explanation : The company would like to keep management overhead to a minimum so RDS would be good to meet that requirement. However, with RDS you cannot access the operating system so the requirement for running scripts on the OS rules RDS out. Therefore, the next best solution is to deploy on an Amazon EC2 instances as the other options presented are unsuitable for a relational database.',
        'Explanation : Elasticity can resolve the issue of underutilization as you can easily and automatically adjust the resource allocations for your compute resources based on actual utilization. This ensures that you have the right amount of resources and do not pay for more than you need.',
        'Explanation : Amazon CloudFront is a content delivery network (CDN) that caches content around the world for lower latency access. AWS Global Accelerator enables access to your application by leveraging the same Edge Locations as CloudFront and routing connections across the AWS global network.',
        'Explanation : Point-in-time recovery (PITR) provides continuous backups of your DynamoDB table data. When enabled, DynamoDB maintains incremental backups of your table for the last 35 days until you explicitly turn it off. It is a customer responsibility to enable PITR on and AWS is responsible for actually performing the backups.',
        'Explanation : Amazon EC2 is an infrastructure as a service (IaaS) solution. This means the underlying hardware and software layer for running a virtual server are managed for you. As a customer you must then manage the operating system and any software you install. This includes installing patches on the operating system as part of regular maintenance activities.',
        'Explanation : With AWS you can pay for what you use and there is no requirement to enter into long term contracts. However, there are opportunities to gain large discounts by committing to 1 or 3 years contracts for reserved instances and savings plans.',
        'Explanation : An Amazon VPC includes multiple Availability Zones. Within a VPC you can create subnets in each AZ that is available in the Region and distribute your resources across these subnets for high availability.',
        'Explanation : AWS are responsible for updating firmware on the physical Amazon EC2 host servers. Customers are then responsible for any patching of the EC2 operating system and any installed software.',
        'Explanation : You can use the consolidated billing feature in AWS Organizations to consolidate billing and payment for multiple AWS accounts. With consolidated billing you get: \nOne bill for multiple accounts. \n Easy tracking or charges across accounts.\nCombined usage across accounts and sharing of volume pricing discounts, reserved instance discounts and savings plans. \nNo extra fee.',
        'Explanation : By using cloud computing, you can achieve a lower variable cost than you can get on your own. Because usage from hundreds of thousands of customers is aggregated in the cloud, providers such as AWS can achieve higher economies of scale, which translates into lower pay as-you-go prices.',
        'Explanation : The most cost-effective solution that works is to use Amazon EC2 instances that are right-sized with the most optimum instance types. Right-sizing is the process of ensuring that the instance type selected for each application provides the right amount of resources for the application.',
        'Explanation : AWS Outposts is a fully managed service that offers the same AWS infrastructure, AWS services, APIs, and tools to virtually any datacenter, co-location space, or on-premises facility for a truly consistent hybrid experience. With AWS Outposts you can extend your VPC into the on-premises data center ',
        'Explanation : The most efficient option is to use multiple EC2 instances and distribute the workload across them. This is an example of horizontal scaling and will allow the workload to keep growing in size without any issue and without increasing the overall processing timeframe.',
        'Explanation : Loose coupling is when you break systems down into smaller components that are loosely coupled together. This reduces interdependencies between systems components. This is achieved in the cloud using messages buses, notification and messaging services. Removing single points of failure ensures fault tolerance and high availability. This is easily achieved in the cloud as the architecture and features of the cloud support the implementation of highly available and fault tolerant systems.',
        'Explanation : The Amazon Simple Storage Service (S3) offers virtually unlimited storage. The total volume of data and number of objects you can store are unlimited. Individual Amazon S3 objects can range in size from a minimum of 0 bytes to a maximum of 5 terabytes. The largest object that can be uploaded in a single PUT is 5 gigabytes.',
        'Explanation : An Amazon EC2 Dedicated Host is a physical server with EC2 instance capacity fully dedicated to your use. Dedicated Hosts allow you to use your existing per-socket, per-core, or per-VM software licenses, including Windows Server, Microsoft SQL Server, SUSE, and Linux Enterprise Server.',
        'Explanation : The Principal element specifies the user, account, service, or other entity that is allowed or denied access to a resource. The bucket policy below has a Principal element set to * which is a wildcard meaning any user. To grant access to a specific IAM user the following format can be used: \n "Principal":{"AWS":"arn:aws:iam::AWSACCOUNTNUMBER:user/username"}',
        'Explanation : To make the deployment highly available the user should launch the instances across multiple Availability Zones in a single AWS Region. Elastic Load Balancers can only serve targets in a single Region so it is not possible to deploy across Regions.',
        'Explanation : The ability to quickly provision resources on AWS is a good example of speed and agility. On AWS the resources are readily available and can be deployed extremely quickly. Scalable compute capacity is another example as it gives you the agility to easily reconfigure your resources with more or less capacity as is required.',
        'Explanation : AWS Batch enables developers, scientists, and engineers to easily and efficiently run hundreds of thousands of batch computing jobs on AWS. AWS Elastic Beanstalk is an easy-to-use service for deploying and scaling web applications and services developed with Java, .NET, PHP, Node.js, Python, Ruby, Go, and Docker on familiar servers such as Apache, Nginx, Passenger, and IIS.',
        'Explanation : Moving the database to Amazon RDS means that the database can take advantage of the built-in Multi-AZ feature. This feature creates a standby instance in another Availability Zone and synchronously replicates to it. In the event of a failure that affects the primary database an automatic failover can occur and the database will become functional on the standby instance.',
        'Explanation : It is a security best practice to rotate access keys regularly. This practice ensures that if access keys are compromised the security exposure is mitigated.',
        'Explanation : Cost allocation tags can be used to tag and categorize your resources and then run view the billing in Cost Explorer and the cost allocation report. For example you can tag your resources by department or project and then view costs attributed to the resources used by those groups.',
        'Explanation : Quick Starts are built by Amazon Web Services (AWS) solutions architects and partners to help you deploy popular technologies on AWS, based on AWS best practices for security and high availability. These accelerators reduce hundreds of manual procedures into just a few steps, so you can build your production environment quickly and start using it immediately. Each Quick Start includes AWS CloudFormation templates that automate the deployment and a guide that discusses the architecture and provides step-by-step deployment instructions.',
        'Explanation : A convertible reserved instance enables you to exchange one or more Convertible Reserved Instances for another Convertible Reserved Instance with a different configuration, including instance family, operating system, and tenancy.',
        'Explanation : Amazon CloudFront is a fast content delivery network (CDN) service that securely delivers data, videos, applications, and APIs to customers globally with low latency, high transfer speeds, all within a developer-friendly environment.',
        'Explanation : Amazon CloudWatch is a performance monitoring service. AWS services send metrics about their utilization to CloudWatch which collects the metrics. You can then view the results in CloudWatch and configure alarms.',
        'Explanation : The most cost-effective approach for ensuring the website is highly available on Amazon EC2 instances is to use an Amazon EC2 Auto Scaling group. This will ensure that the appropriate number of instances is always available to service the demand. An Elastic Load Balancer can be placed in front of the instances to distribute incoming connections.',
        'Explanation : There are a several security best practices for AWS IAM that are listed in the document shared below. Enabling multi-factor authentication is a best practice to require a second factor of authentication when logging in. Another best practice is to grant least privilege access when configuring users and password policies.',
        'Explanation : AWS Cost Explorer has an easy-to-use interface that lets you visualize, understand, and manage your AWS costs and usage over time. AWS Cost Explorer provides you with a set of default reports that you can use as the starting place for your analysis. From there, use the filtering and grouping capabilities to dive deeper into your cost and usage data and generate custom insights.',
        'Explanation : Two of the benefits of using a managed Amazon RDS service instead of a self-managed database on EC2 are that you get automated backups and automatic software patching.',
        'Explanation : Amazon Macie is a fully managed data security and data privacy service that uses machine learning and pattern matching to discover and protect your sensitive data in AWS. Amazon Macie automates the discovery of sensitive data at scale and lowers the cost of protecting your data. Macie automatically provides an inventory of Amazon S3 buckets including a list of unencrypted buckets, publicly accessible buckets, and buckets shared with AWS accounts outside those you have defined in AWS Organizations. Then, Macie applies machine learning and pattern matching techniques to the buckets you select to identify and alert you to sensitive data, such as personally identifiable information (PII).',
        'Explanation : AWS CodeCommit is a fully-managed source control service that hosts secure Git-based repositories. It makes it easy for teams to collaborate on code in a secure and highly scalable ecosystem. CodeCommit eliminates the need to operate your own source control system or worry about scaling its infrastructure. You can use CodeCommit to securely store anything from source code to binaries, and it works seamlessly with your existing Git tools.',
        'Explanation : The AWS Cloud Development Kit (AWS CDK) is an open source software development framework to define cloud application resources using familiar programming languages. With AWS CDK you can stick to using programming languages that are familiar to you and have infrastructure deployed using AWS CloudFormation.',
        'Explanation : Scheduled scaling helps you to set up your own scaling schedule according to predictable load changes. For example, lets say that every week the traffic to your web application starts to increase on Wednesday, remains high on Thursday, and starts to decrease on Friday. You can configure a schedule for Amazon EC2 Auto Scaling to increase capacity on Wednesday and decrease capacity on Friday.',
        'Explanation : There are several ways to launch resources in AWS. You can use the AWS Management Console or Command Line Interface (CLI) or you can automate the process by using tools such as AWS CloudFormation. With AWS CloudFormation you can deploy infrastructure such as Amazon ElastiCache clusters by defining your desired configuration state in code using a template file written in JSON or YAML. CloudFormation will then deploy the resources by creating a Stack according to the template file.',
        'Explanation : An Amazon Machine Image (AMI) provides the information required to launch an instance. You must specify an AMI when you launch an instance. You can launch multiple instances from a single AMI when you need multiple instances with the same configuration. You can use different AMIs to launch instances when you need instances with different configurations.',
        'Explanation : AWS Trusted Advisor is an online tool that provides you real time guidance to help you provision your resources following AWS best practices. Trusted Advisor checks help optimize your AWS infrastructure, improve security and performance, reduce your overall costs, and monitor service limits.',

}

main()

while play_again:
    main()

print("BYYYEEE")
