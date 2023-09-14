from helpers.helpers import (
    write_to_file,
    fix_title,
    dev_soup,
    write_to_json,
    dump_to_json,
)


url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"

soup = dev_soup(url)

flicks = soup.findAll(
    "li", class_="ipc-metadata-list-summary-item sc-59b6048d-0 jemTre cli-parent"
)
results = []
for flick in flicks:
    title = flick.find("h3").text.split(". ")[1:]
    title = fix_title(title)
    rank = flick.find("h3").text.split(". ")[0]
    date = (
        flick.find("div", class_="sc-b51a3d33-5 ibuRZu cli-title-metadata")
        .findAll("span")[0]
        .text
    )

    running_time = (
        flick.find("div", class_="sc-b51a3d33-5 ibuRZu cli-title-metadata")
        .findAll("span")[1]
        .text
    )

    try:
        rating = (
            flick.find("div", class_="sc-b51a3d33-5 ibuRZu cli-title-metadata")
            .findAll("span")[2]
            .text
        )
    except IndexError:
        rating = "Not Rated"

    result = {
        "rank": rank,
        "title": title,
        "date": date,
        "running_time": running_time,
        "rating": rating,
    }
    results.append(result)
    write_to_file(result)
    write_to_json(result)

dump_to_json(results)
