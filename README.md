Decode the contents of the Ontario Proof of Vaccination (the "Smart Health Card QR Code")

## Output

This is from my QR code, hopefully fully redacted although I suspect it tells
you what kind of doses I got.

```json
{
  "iss": "https://prd.pkey.dhdp.ontariohealth.ca",
  "nbf": 1634342670.448,
  "vc": {
    "type": [
      "https://smarthealth.cards#health-card",
      "https://smarthealth.cards#immunization",
      "https://smarthealth.cards#covid19"
    ],
    "credentialSubject": {
      "fhirVersion": "4.0.1",
      "fhirBundle": {
        "resourceType": "Bundle",
        "type": "collection",
        "entry": [
          {
            "fullUrl": "resource:0",
            "resource": {
              "resourceType": "Patient",
              "name": [
                {
                  "family": "FAMILY NAME",
                  "given": [
                    "FIRST NAME",
                    "MIDDLE NAMES"
                  ]
                }
              ],
              "birthDate": "YYYY-MM-DD"
            }
          },
          {
            "fullUrl": "resource:1",
            "resource": {
              "resourceType": "Immunization",
              "meta": {
                "security": [
                  {
                    "system": "https://smarthealth.cards/ial",
                    "code": "IAL1.4"
                  }
                ]
              },
              "status": "completed",
              "manufacturer": {
                "identifier": {
                  "system": "http://hl7.org/fhir/sid/mvx",
                  "value": "MOD"
                }
              },
              "vaccineCode": {
                "coding": [
                  {
                    "system": "http://hl7.org/fhir/sid/cvx",
                    "code": "207"
                  },
                  {
                    "system": "http://snomed.info/sct",
                    "code": "28571000087109"
                  }
                ]
              },
              "occurrenceDateTime":  "YYYY-MM-DD",
              "lotNumber": "DDDDDDD",
              "patient": {
                "reference": "resource:0"
              },
              "performer": [
                {
                  "actor": {
                    "display": "ON, Canada"
                  }
                }
              ]
            }
          },
          {
            "fullUrl": "resource:2",
            "resource": {
              "resourceType": "Immunization",
              "meta": {
                "security": [
                  {
                    "system": "https://smarthealth.cards/ial",
                    "code": "IAL1.4"
                  }
                ]
              },
              "status": "completed",
              "manufacturer": {
                "identifier": {
                  "system": "http://hl7.org/fhir/sid/mvx",
                  "value": "MOD"
                }
              },
              "vaccineCode": {
                "coding": [
                  {
                    "system": "http://hl7.org/fhir/sid/cvx",
                    "code": "207"
                  },
                  {
                    "system": "http://snomed.info/sct",
                    "code": "28571000087109"
                  }
                ]
              },
              "occurrenceDateTime": "YYYY-MM-DD",
              "lotNumber": "DDDDDDD",
              "patient": {
                "reference": "resource:0"
              },
              "performer": [
                {
                  "actor": {
                    "display": "ON, Canada"
                  }
                }
              ]
            }
          }
        ]
      }
    }
  }
}
```


## Setup

This runs in python3.
**I strongly suggest you set up a virtualenv before installing any python packages**. Check one of these guides:

 - https://realpython.com/python-virtual-environments-a-primer/
 - https://docs.python-guide.org/dev/virtualenvs/
 - https://towardsdatascience.com/virtual-environments-for-absolute-beginners-what-is-it-and-how-to-create-one-examples-a48da8982d4b

(If you're new to python, I appologize for the mess that is package management in python)

We need a JWT library, PyJWT seems to be the top python library.
Sadly it doesn't support the body being compressed as happens with SHC.
Thankfully, someone has created a fix for this, but it hasn't merged yet.
https://github.com/jpadilla/pyjwt/pull/666

```
pip install 'git+https://github.com/Roguelazer/pyjwt.git@deflate#egg=pyjwt[crypto]'
```

OR

```
pip install -r requirements.txt
```

## Refs
 - https://www.roguelazer.com/2021/06/cdph-digital-vaccine-record/#fnref:pip-install
 - https://mikkel.ca/blog/digging-into-quebecs-proof-of-vaccination/
