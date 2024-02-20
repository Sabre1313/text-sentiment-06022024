{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6d1f41d9-cac5-4b63-9ba9-8eebbcd57a65",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app '__main__'\n",
      " * Debug mode: off\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.\n",
      " * Running on http://127.0.0.1:5000\n",
      "Press CTRL+C to quit\n",
      "127.0.0.1 - - [06/Feb/2024 11:22:22] \"GET / HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [06/Feb/2024 11:22:23] \"GET /favicon.ico HTTP/1.1\" 404 -\n",
      "127.0.0.1 - - [06/Feb/2024 11:22:36] \"POST /result HTTP/1.1\" 200 -\n"
     ]
    }
   ],
   "source": [
    "from flask import Flask,request,render_template\n",
    "from textblob import TextBlob\n",
    "\n",
    "app = Flask(__name__)\n",
    "\n",
    "@app.route(\"/\",methods=[\"GET\",\"POST\"])\n",
    "def index():\n",
    "    return(render_template(\"index.html\"))\n",
    "\n",
    "@app.route(\"/result\",methods=[\"GET\",\"POST\"])\n",
    "def result():\n",
    "    t = request.form.get(\"t\")\n",
    "    result = TextBlob(t).sentiment\n",
    "    return(render_template(\"result.html\",result=result))\n",
    "\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    app.run()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b6f9f3c2-2c8e-4878-89d7-359ebb179436",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
