# Part 1
import pprint 

def read_csv(filename):
  """
  Parameters
  ----------
  read_csv(filename: csv)
      list of information of pre u students over the years

  Returns
  -------
  list 
    a list of the header and a list of list of the info of the students enrolled
  """
    # Type your code below
  data = []
  with open(filename) as f:
      header = f.readline().strip().split(",")
      for lines in f.readlines():
        record = lines.strip().split(",")
        record[0] = int(record[0])
        record[3] = int(record[3])
        data.append(record)
      return header, data
#pprint.pprint(read_csv("pre-u-enrolment-by-age.csv"))


# Part 2
def filter_gender(enrolment_by_age, sex):
  """
  Parameters
  ----------
      list and string
          list of the info on the pre-u students and the gender
        

  Returns
  -------
  list
    a filtered list with the sex column filtered depending on the input of sex
  
  """
    # Type your code below
  new_data = []
  for rec in enrolment_by_age:
    if rec[2] == sex:
        new_data.append([rec[0], rec[1], rec[3]])
  return new_data

# Part 3

def sum_by_year(enrolment_data):
    """
    Parameters
    ----------
    list
        a list of the enrolment data of pre-u students
    Returns
    -------
    list
        a new list with only the year column and a new column totaling the number of enrolments.
    """
    # Type your code below
    sum = 0
    list_sum = []
    list_year = []
    list_year.append(enrolment_data[0][0])
    for rec in enrolment_data:
        year = rec[0]
        if year not in list_year:
            
            list_year.append(year)
            list_sum.append(sum)
            sum = 0
            
        sum += rec[2]
    list_sum.append(sum)
    new_data = []
    for i in range(len(list_year)):
    
        new_data.append([list_year[i], list_sum[i]])
    return new_data
    
head, enrolment = read_csv("pre-u-enrolment-by-age.csv")
enrolment_data = filter_gender(enrolment, "MF")

pprint.pprint(sum_by_year(enrolment_data))
# Part 4

def write_csv(filename, header, data):
    """
    Parameters
    ----------
      csv and list 
         the file pre-u-enrolment and the header and data of the file 
    Returns
    ---------
     an integer counting the number of lines written
    file
    """
    # Type your code below
    #total enrolment in the question refers to the sum of enrolment a year, which is found in part 3.
    # As such the output of the function when u print it would be
#>>>>[header, total_enrolment_per_year]
    #[1984, 21471]------> the function counts this as 1 and so on
    #with the final output will be 35 the total number of lines
    with open(filename, "w") as f:
        
        output = ",".join(header) + "\n" 
        count = 0
        for rec in data:
            #the header should contain the year and total enrolment as stated in the readme.md
        #Everytime a line is written , 1 is added to the count.
            output = f'{rec[0]}{rec[1]}n'
            f.write(output)
            count += 1
        return count
        
        
        
"""

# TESTING
# You can write code below to call the above functions
# and test the output
read_csv("pre-u-enrolment-by-age.csv")
"""