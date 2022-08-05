import json

import cloudscraper
import re


class TrendyolServiceCrawler:
    def __init__(self):
        self._serviceName = "TrendyolServiceCrawler"
        self._crawlerUrl: str = None

        self._success: bool = False
        self._detailModel = dict(
            tUrl=None,
        )

    def setCrawlerUrl(self, _crawlerUrl: str = None):
        self._crawlerUrl = _crawlerUrl

    def crawlerDetail(self):
        try:
            scraper = cloudscraper.create_scraper(
                browser={
                    'browser': 'firefox',
                    'platform': 'windows',
                    'mobile': False
                }
            )
            setAvailableResponseText = scraper.get(self._crawlerUrl).text
            setAvailableResponseText = setAvailableResponseText.replace('\r', '').replace('\n', '').replace('\t', '')
            setAvailableResponseText = re.sub(r"\s+", " ", setAvailableResponseText)
            return True, setAvailableResponseText
        except Exception as e:
            print(e)
            return False, None

    def getDetail(self):
        availableResponseSuccess, availableResponseText = self.crawlerDetail()
        if availableResponseSuccess is True:
            self._detailModel.__setitem__("tUrl", self._crawlerUrl)

            searchProductDetail = re.findall(r"""<script type="application/javascript">window.__PRODUCT_DETAIL_APP_INITIAL_STATE__=(.*?);""", availableResponseText, re.MULTILINE)
            if len(searchProductDetail) > 0:
                searchProductArr = json.loads(searchProductDetail[0])

                self._detailModel.__setitem__("tName", searchProductArr["product"]["name"])
                self._detailModel.__setitem__("tBrand", searchProductArr["product"]["brand"]["name"])
                self._detailModel.__setitem__("tPriceSell", searchProductArr["product"]["price"]["sellingPrice"]["value"])
                self._detailModel.__setitem__("tPriceDiscount", searchProductArr["product"]["price"]["discountedPrice"]["value"])
                self._detailModel.__setitem__("tCategory", searchProductArr["product"]["category"]["hierarchy"])
                self._detailModel.__setitem__("tMerchantName", searchProductArr["product"]["merchant"]["name"])
                self._detailModel.__setitem__("tMerchantCity", searchProductArr["product"]["merchant"]["cityName"])
                self._detailModel.__setitem__("tMerchantSellerScore", searchProductArr["product"]["merchant"]["sellerScore"])

                iOtherMerchantArr = []
                for iOtherMerchant in searchProductArr["product"]["otherMerchants"]:
                    iOtherMerchantArr.append(dict(
                        tMerchantName=iOtherMerchant["merchant"]["name"],
                        tMerchantCity=iOtherMerchant["merchant"]["cityName"],
                        tMerchantSellerScore=iOtherMerchant["merchant"]["sellerScore"],
                    ))
                self._detailModel.__setitem__("tOtherMerchant", json.dumps(iOtherMerchantArr))

                return self._detailModel
            else:
                return False

        else:
            return None

