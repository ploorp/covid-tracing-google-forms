# Google Forms submission script (unfinished)

I made this little script while I was learning python. At my high school we had a google form that for some reason was supposed to be filled out every period (8 or 9 times per day), as it turns out you can submit google forms using only URL params and a POST request, so i decided to try doing it. I made the script interactive in order to support A/B days and a custom number of requests. Obviously these could be implemented as arguments.

### Other solutions
- Google Cloud
- Google Cloud API + Python
- Browser automation (Selenium)

If you are curious [here](https://news.ycombinator.com/item?id=2883863) is a comparison of [requests](https://github.com/psf/requests) and [httplib2](https://github.com/httplib2/httplib2)

---

### Related links

- [college attendance script](https://github.com/jamesshah/GoogleForm-AutoFill)
  - [article about the script](https://dev.to/jamesshah/how-i-automated-the-google-form-filling-for-my-college-attendance-using-python-3ao1)
     - [the comments from the article](https://dev.to/jamesshah/how-i-automated-the-google-form-filling-for-my-college-attendance-using-python-3ao1#comments)
- [Selenium method](https://t[renegadecoder.com/code/write-a-python-script-to-autogenerate-google-form-responses/)
- [Google Forms API](https://developers.google.com/forms/api)
  - [Google API Python client library](https://github.com/googleapis/google-api-python-client)
  - [code samples](https://github.com/googleworkspace/python-samples/tree/main/forms)
