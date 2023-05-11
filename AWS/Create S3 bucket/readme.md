# S3
Amazon Simple Storage Service (Amazon S3) is an object storage service offering industry-leading scalability, data availability, security, and performance. Customers of all sizes and industries can store and protect any amount of data for virtually any use case, such as data lakes, cloud-native applications, and mobile apps. With cost-effective storage classes and easy-to-use management features, you can optimize costs, organize data, and configure fine-tuned access controls to meet specific business, organizational, and compliance requirements.</h2>


<h2> How to create an S3 bucket </h2>
<p>Step1.
Search for S3 service in AWS and click on create bucket option. </p>

![s3 main page](https://user-images.githubusercontent.com/94166344/236614303-9dda1e67-97b6-490e-b39b-4bb56bb50b21.png)


<p>Step 2.
  In “general configuration”
  <ul>
  <li>a. As S3 is a global service, so give a name like it will be globally unique.
/li>
  <li>b. select the region
</li>
  <li>In the “Object Ownership”
Keep everything as default</li>
  <li>In the “Block Public Access settings for this bucket”
Keep everything as default
</li>
    <li>In the “Bucket Versioning”
Keep everything as default</li>
    <li>In the “Default encryption”
Make Bucket Key as disable, and keep everything as default</li>
</ul>
</p>

![create bucket config](https://github.com/hrishikesh26/Projects/assets/94166344/8679bb12-62e7-4780-93f9-b5f01bebc9ec)

<p>At last click on create bucket
  
![Successfully created the bucket](https://user-images.githubusercontent.com/94166344/236632565-065dcdbb-6b1b-430f-bc58-43fd8d4c70b2.png)
  
  Now you can select that bucket and upload any file you want.
For uploading follow the sequence as bellow

  [Name of Bucket] ”auniquebucketforpractice” > upload > add file/ add folder > [select any file
you want] > upload.

  
  ---------------------------------------------------------------------------------------------
  
</p>

<h2># How to unable the bucket versioning.</h2>

<p>1. While creating the new bucket do the settings the same as mentioned above’s Step2
Just in the “Bucket Versioning”
       Enable the option of bucket versioning.
2. If you want to enable versioning in the existing bucket, follow the instruction mentioned
below.
[Name of Bucket] ”auniquebucketforpractice” > Properties > Bucket Versioning > edit > enable >
save changes.</p>


![bucket versioning](https://user-images.githubusercontent.com/94166344/236632718-21c0b84a-ac24-4483-a6d0-527ccf8d7a3d.png)

<p>After enabling versioning you can see all the versions of the same file that are uploaded before.
</p>

![view buckets](https://github.com/hrishikesh26/Projects/assets/94166344/cb7b154c-49cc-42aa-8e36-b5969bbfeddb)


------------------------------------------------------------------------------------------------

<h2># Presigned URL</h2>

<p>As the bucket which is created is private, so no one can access the data from this. If you want to
share some data for a specific amount of time then you can use share using Presigned URL
For making this happen, follow bellow steps as mentioned.
Select the file in a bucket that you want to share > Click on Actions > Share with a presigned
URL > specify the number of minutes/hours you want to share > click to create presigned URL.</p>


![use presigned url](https://user-images.githubusercontent.com/94166344/236632808-5da9419e-600b-4b7b-a73e-6690f9b4b21e.png)

Then copy the presigned URL and paste on the web browser.


-----------------------------------------------------------------------------------------------

<h2># Making Bucket Public using ACL</h2>

<p>Amazon S3 access control lists (ACLs) enable you to manage access to buckets and objects.
Each bucket and object has an ACL attached to it as a subresource. It defines which AWS
accounts or groups are granted access and the type of access. 

Step1. 
  Search for s3 service in AWS and click on create bucket option
  
Step 2.
  In "general configuration"
  <ul>
    <li>As S3 is a global service, so give a name like it will be globally unique.
</li>
    <li>select the region</li>![object ACL](https://user-
    
</ul>

In the "Object Ownership"
  Select the option as ACLs enabled
  
![object ACL](https://github.com/hrishikesh26/Projects/assets/94166344/7e08c6fb-1e6c-4122-b290-d74c85b28f83)

In the “Block Public Access settings for this bucket”
Unchecked the Block all Public Access
And click on the acknowledgment of warning.
</p>

![block all public access](https://github.com/hrishikesh26/Projects/assets/94166344/8567e0c9-3a62-4489-943f-dca8d4100549)

<p> In the “Bucket Versioning”
Enable the bucket versioning.
In the “Default encryption”
Make Bucket Key ad disable and keep everything as default
At last click on create bucket.
Upload any file into the bucket.
For uploading follow the sequence as bellow
[Name of Bucket] ”apublicbucketforpractice” > upload > add file/ add folder > [select any file you
want] >Permissions > checked Specify individual ACL permissions > Acknowledge the warning
tag > upload.
</p>

![specify individual acl](https://github.com/hrishikesh26/Projects/assets/94166344/4ded5d59-067a-441a-a397-183be0b6c3c7)

For checking whether the file is public or not
Select the file in the bucket and click on copy url and paste url in web browser.

If you missed above settings at the time of file upload then follow below steps.
select the file > actions > Make public using ACL > Make public.


![make objects public](https://github.com/hrishikesh26/Projects/assets/94166344/678a0a37-5b78-4ef1-8322-908921f30073)

Again cross check by selecting the file in the bucket and clicking on copy URL and paste URL in
the web browser

