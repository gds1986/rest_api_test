## Testcases
* Testcases are automated using Python's `requests` package
* Validations are done using python `assert` statements
* All testcases validate that the response code is `200`
* Other validations include format checks according to docs/examples provided on https://github.com/thundercomb/poetrydb#readme
For more details, please refer below tables and test code in `tests` folder

**Please note:**
A couple of test cases failed due to difference between expected format given in docs as compared to actual format.
For example, `/linecount/3` request expected linecount to be an integer in the response, but string value is returned in actual.

### Author
| Test case | Request url                                         | Expected Response                                                                      | Description/Reason for this validation                                                                                                   |
|-----------|-----------------------------------------------------|----------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| test_1    | `/author`                                           | non-empty list of authors                                                              | there should not be empty authors data in the response; asserted that length of "authors" field is greater than 0                        |                                     
| test_2    | `/author/Ernest Dowson`                             | Author name `Ernest Dowson` in all poem objects                                        | Input and output data (Author name) should match in all poem objects                                                                     |
| test_3    | `/author/owson/author`                              | Only `author` field present with matching sub-string value `owson` in all list objects | Only expected output fields should be present; Response data (Author name) should have matching value as input value in all list objects |
| test_4    | `/author/Ernest Dowson:abs/author`                  | Only `author` field present with exact value `Ernest Dowson` in all list objects       | Only expected output fields should be present; Response should have exact value as input                                                 |
| test_5    | `/author/Ernest Dowson/author,title,linecount`      | Only `author, title, linecount` fields are present                                     | Only expected output fields should be present in the response                                                                            |
| test_6    | `/author/Ernest Dowson/author,title,linecount.text` | Only `author, title, linecount` fields are present in text form                        | Only expected output fields should be present; Response should be in text form; Empty strings are filtered out                           |

### Title
| Test case | Request url                                            | Expected Response                                                                                     | Description/Reason for this validation                                                                                             |
|-----------|--------------------------------------------------------|-------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| test_1    | `/title`                                               | non-empty list of titles                                                                              | there should not be empty titles data in the response; asserted that length of "titles" field is greater than 0                    |                                     
| test_2    | `/title/Ozymandias`                                    | Title `Ozymandias` in all poem objects                                                                | Input and output data (title) should match in all poem objects                                                                     |
| test_3    | `/title/spring/title`                                  | Only `title` field present with matching string `spring` in all list objects, case ignored            | Only expected output fields should be present; Response data (title) should have matching value as input value in all list objects |
| test_4    | `/title/In spring and summer winds may blow:abs/title` | Only `title` field present with exact value `In spring and summer winds may blow` in all list objects | Only expected output fields should be present; Response should have exact value as input in all list objects                       |
| test_5    | `/title/Ozymandias/author,title,linecount`             | Only `author, title, linecount` fields are present                                                    | Only expected output fields should be present in the response                                                                      |
| test_6    | `/title/Ozymandias/title,lines.text`                   | Only `author, title, linecount` fields are present in text form                                       | Only expected output fields should be present; Response should be in text form; Empty strings are filtered out                     |

### Lines
| Test case | Request url                                             | Expected Response                                                           | Description/Reason for this validation                                                                         |
|-----------|---------------------------------------------------------|-----------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| test_1    | `/lines/Latitudeless Place`                             | `lines` field should have sub-text `Latitudeless Place` in all poem objects |                                                                                                                |                                     
| test_2    | `/lines/Latitudeless Place/author`                      | Only `author` field present with value `Emily Dickinson` is returned        | Only expected output fields should be present; Data validation is also done                                    |
| test_3    | `/lines/Latitudeless Place/author,title,linecount`      | Only `author, title, linecount` fields are present                          | Only expected output fields should be present in the response                                                  |
| test_4    | `/lines/Latitudeless Place/author,title,linecount.text` | Only `author, title, linecount` fields are present in text form             | Only expected output fields should be present; Response should be in text form; Empty strings are filtered out |

### Linecount
| Test case | Request url       | Expected Response                                                       | Description/Reason for this validation                                                                                   |
|-----------|-------------------|-------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| test_1    | `/linecount/3`    | Number of `lines` is 3 and `linecount` value is `3` in each poem object | This test is failing because expected format of linecount is integer as per docs, but string value is returned in actual |

### Poemcount
| Test case | Request url                                            | Expected Response                                                                                                          | Description/Reason for this validation                           |
|-----------|--------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------|
| test_1    | `/author,poemcount/Dickinson;2`                        | `2` poem objects with `author` field having matching name `Dickinson`                                                      |                                                                  |
| test_2    | `/author,poemcount/Dickinson;2/author,title,linecount` | `2` poem objects with `author` field having matching name `Dickinson` and only `author, title, linecount` fields in result | Only expected output fields with matching data should be present |

### Random
| Test case | Request url                        | Expected Response                                                             | Description/Reason for this validation        |
|-----------|------------------------------------|-------------------------------------------------------------------------------|-----------------------------------------------|
| test_1    | `/random/3`                        | `3` random poem objects                                                       |                                               |
| test_2    | `/random/3/author,title,linecount` | `3` random poem objects with only `author, title, linecount` fields in result | Only expected output fields should be present |

### Combinations
| Test case | Request url                                     | Expected Response                                                                                                                                          | Description/Reason for this validation                                                                                   |
|-----------|-------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| test_1    | `/title,random/Sonnet;3`                        | `3` random poem objects where each object has `title` field having sub-text `Sonnet`                                                                       |                                                                                                                          |
| test_2    | `/title,author,linecount/Winter;Shakespeare;18` | n number of poem objects with `title` field having sub-text `Winter`, `author` field having sub-text `Shakespeare` and `linecount` field having value `18` | This test is failing because expected format of linecount is integer as per docs, but string value is returned in actual |
