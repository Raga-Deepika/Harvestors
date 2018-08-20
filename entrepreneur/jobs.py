from entrepreneur.base import entre_main


def entre_jobs():
    category_name = ['patents', 'mergers-and-acquisitions', 'class-action-lawsuits']
    page_no = range(1, 15)
    for c in category_name:
        for p in page_no:
            return entre_main(c, p)