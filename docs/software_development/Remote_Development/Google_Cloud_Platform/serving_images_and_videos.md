# Serving Images and Videos From A Bucket

## General Use

Occasionally in a web application there are images and/or videos that need to be frequently added or updated. This tends to be the case when the images served in an application are attached to a database with entries that are continously being added to or changing. Typically when serving images in the front-end from a database entry, we would need to add an image to the code repository every time we want to add a new database entry. However, serving images from a GCS Buckets can help speed up the process of adding images for new entries in a database collection to your project by removing the step of pushing new images to your code repository.

## Example

For the [BHK lab website](https://bhklab.ca/) we have database collections for our team members, important publications, presentations, and preprints which need to be frequently updated. If images were stored locally within the project's image folder for these sections, there would be many hurdles in the way of adding or updating entries in our database (containing images) and having the changes reflect in the deployed application. This is because not only would we need to adjust our database with the new update/entry, we would also need to add the image to the project repository and then redeploy our application. 

For example, in the case where we want to add or update a member from the Caboodle (bhklab) database we only need to execute the following two steps when utilizing GCS for image serving:

1. Have a new database entry created:
	```js
		{
			"_id": {
				"$oid": "67dc262b7658e91803c89099"
			},
			"name": "Matthew Boccalon",
			"slug": "Matthew_Boccalon",
			"preferredName": "",
			"position": "Software Developer",
			"bio": "Matthew completed his undergrad at York University in computer science. He has an adept understanding of various languages, technologies, and frameworks that aid him in his passion for full stack development. Matthew has previously worked at Lymphoma Canada as their Donor Database Manager and has now pivoted into full stack development here in the BHK lab.",
			"preferredEmail": "matthew.boccalon@uhn.ca",
			"socials": {
				"twitter": "https://twitter.com/MatthewBHKLab",
				"bluesky": "",
				"linkedIn": "https://www.linkedin.com/in/matthew-boccalon-1b96791a2/"
			},
			"image": "matthew_boccalon.png"
		}
	```

2. Upload image to GCS bucket referenced for displaying members in the code

![caboodle-member-bucket](images/caboodle-image.png){: style="height:100%;width:100%"}

The updated member will immediately render on the lab website in the current members section. The aftermath looks something like the following, without having to redeploy the application:

![caboodle-member-bucket](images/current-member.png){: style="height:395px;width:245px"}


### Something To Keep In Mind

When referencing a GCS bucket for an image, it's important to invoke the current date function as added below to make sure the most recent images are always referenced. This is because browsers tend to cache GCS images, to avoid this and to ensure displaying the most recent version of a sourced image, you tack on ```?v=${new Date().getTime()}``` to the end of the src string.

```js
<img src={`https://storage.googleapis.com/caboodle-images/member-photos/${item.image}?v=${new Date().getTime()}`}>
```

