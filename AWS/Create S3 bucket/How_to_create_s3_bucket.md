<h2>S3
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
</ul>![create bucket config](https://user-images.githubusercontent.com/94166344/236632471-969f4575-1319-4823-9952-241b17da3940.png)
</p>

<p>At last click on create bucket
  
![Successfully created the bucket](https://user-images.githubusercontent.com/94166344/236632565-065dcdbb-6b1b-430f-bc58-43fd8d4c70b2.png)
  
  Now you can select that bucket and upload any file you want.
For uploading follow the sequence as bellow

  [Name of Bucket] ”auniquebucketforpractice” > upload > add file/ add folder > [select any file
you want] > upload.

  
  ---------------------------------------------------------------------------------------------
  
</p>

<h2># How to unable the bucket versioning.</h2>

<p>$$$ While creating the new bucket do the settings the same as mentioned above’s Step2
Just in the “Bucket Versioning”
Enable the option of bucket versioning.
$$$ If you want to enable versioning in the existing bucket, follow the instruction mentioned
below.
[Name of Bucket] ”auniquebucketforpractice” > Properties > Bucket Versioning > edit > enable >
save changes.</p>


![bucket versioning](https://user-images.githubusercontent.com/94166344/236632718-21c0b84a-ac24-4483-a6d0-527ccf8d7a3d.png)

<p>After enabling versioning you can see all the versions of the same file that are up![view buckets](https://user-images.githubusercontent.com/94166344/236632758-06051e32-9549-4f43-a389-bc50bb09b946.png)
loaded before.
</p>

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
  
  images.githubusercontent.com/94166344/236633001-764f7a9d-e511-4683-887e-54b0b0dc25f1.png)

In the “Block Public Access settings for this bucket”
Unchecked the Block all Public Access
And click on the acknowledgment of warning.


</p>![make objects public](https://user-images.githubusercontent.com/94166344/236633044-e77301d3-b44f-49f5-959f-04ffbfab915f.png)

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





