from crawler.crawler import fetch_page

from detectors.cms_detector import detect_cms
from detectors.pixel_detector import detect_pixels
from detectors.video_detector import detect_video_platform
from detectors.automation_detector import detect_automation
from detectors.checkout_detector import detect_checkout

from report.report_generator import generate_report


def scan_site(url):

    html = fetch_page(url)

    results = {}

    results["CMS"] = detect_cms(html)
    results["Pixels"] = detect_pixels(html)
    results["Video Platform"] = detect_video_platform(html)
    results["Automation Tools"] = detect_automation(html)
    results["Checkout Platforms"] = detect_checkout(html)

    return results


if __name__ == "__main__":

    url = input("Digite a URL do site: ")

    data = scan_site(url)

    generate_report(data)
