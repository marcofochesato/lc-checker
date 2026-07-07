from app.extractors.invoice import extract_invoice

if __name__ == "__main__":

    sample_text = """
    Invoice 12345
    Date: 01/07/2026
    Seller: ABC Leather Spa
    Buyer: XYZ Trading Ltd
    Currency: USD
    Amount: 45814.16
    Incoterm: CIP Phnom Penh
    """

    result = extract_invoice(sample_text)

    print(result)
