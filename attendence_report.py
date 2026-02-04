{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "221ab4cd-a9fb-4942-9996-31601ae24ca9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "attendence report of students\n",
      "name:Avinash\n",
      "present:20/25\n",
      "attendence:80.00%\n",
      "\n",
      "name:Anjali\n",
      "present:22/25\n",
      "attendence:88.00%\n",
      "\n",
      "name:Dileep\n",
      "present:18/25\n",
      "attendence:72.00%\n",
      "\n",
      "name:Neha\n",
      "present:24/25\n",
      "attendence:96.00%\n",
      "\n",
      "name:Kiran\n",
      "present:21/25\n",
      "attendence:84.00%\n",
      "\n",
      "\n",
      "In 40 Seconds WhatsApp will open and after 8 Seconds Message will be Delivered!\n"
     ]
    }
   ],
   "source": [
    "import pywhatkit as pt\n",
    "students=[ {\"name\": \"Avinash\", \"present_days\": 20, \"total_days\": 25},\n",
    "    {\"name\": \"Anjali\", \"present_days\": 22, \"total_days\": 25},\n",
    "    {\"name\": \"Dileep\", \"present_days\": 18, \"total_days\": 25},\n",
    "    {\"name\": \"Neha\", \"present_days\": 24, \"total_days\": 25},\n",
    "    {\"name\": \"Kiran\", \"present_days\": 21, \"total_days\": 25} ]\n",
    "report=\"attendence report of students\\n\"\n",
    "for s in students:\n",
    "    percentage=(s['present_days'] / s['total_days'])*100\n",
    "    report+=f\"name:{s['name']}\\n\"\n",
    "    report+=f\"present:{s['present_days']}/{s['total_days']}\\n\"\n",
    "    report+=f\"attendence:{percentage:.2f}%\\n\\n\"\n",
    "print(report)\n",
    "pt.sendwhatmsg('+919550544124',report,13,10,8,False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "75d2bf74-97f1-492f-bc62-e8217ced9c9b",
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
   "version": "3.14.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
