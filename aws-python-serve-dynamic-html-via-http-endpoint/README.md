# FrameWork used
We have used Flask to implement api and render HTML response.

# How it works.
For now we have only one endpoing "/test" which will call our TestParsing class handle function.

It will check below things.
1. Check Authorization key is there on headers
2. Check valid token provided in Authorization.(For now valid token is something which 
have email and username in it. Later we will extend it to check whether email we get after decoding
JWT is present in our DB or not.)

# Setting things up.

We have local.py which we won't push on git it will have secret key of our JWT. Later we will set SSM variable.

To run this in your local machine.
1. Install dependencies in requirements.txt
2. add local.py in code directory.
3. Add SECRET_KEY= in that.