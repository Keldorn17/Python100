import pandas
import requests
from bs4 import BeautifulSoup


def main() -> None:
    url = 'https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors'
    response = requests.get(url=url).text
    soup = BeautifulSoup(response, 'html.parser')
    table_titles = soup.find_all(name='th')
    titles = [title.getText().strip() for title in table_titles]
    table_rows = soup.find_all(name='tr')
    data = [row_data.getText() for row_data in table_rows][1:]
    data_list: list[dict[str, str]] = []
    for row in data:
        splits = row.split(':')
        data_list.append({
            titles[0]: splits[1].split('Major')[0],
            titles[1]: splits[2].split('Degree Type')[0],
            titles[2]: splits[3].split('Early Career Pay')[0],
            titles[3]: splits[4].split('Mid-Career Pay')[0].replace(',', '').replace('$', '').strip(),
            titles[4]: splits[5].split('% High Meaning')[0].replace(',', '').replace('$', '').strip(),
            titles[5]: splits[6].split('%')[0]
        })

    df = pandas.DataFrame(data=data_list)
    # df = df.set_index('Rank')


if __name__ == '__main__':
    main()
