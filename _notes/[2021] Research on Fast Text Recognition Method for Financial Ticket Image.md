- 20210112
----

![](<[2021] Research on Fast Text Recognition Method for Financial Ticket Image/paper_title.png>)

论文的核心在于 Figure 2 和 Figure 3. 另外 Table 1 也很重要.

本文将 Financial ticket 分为三类:
1) I-A (Fixed form, simple vocabulary) types: toll invoices, taxi invoices, quota invoices, value-added tax Invoices.
2) I-B (Fixed form, complex vocabulary): train tickets, plane itinerary tickets.
3) II (Non-fixed forms): bank receipts, voucher tickets.

## 论文摘记
> However, it can be seen from the above formula (Smooth L1 Loss) that the four vertex coordinates of the predicted bounding box are used in the regression of the prediction box, and the loss of the four points is independently calculated. This operation ignores the relationship between the four vertices, which will cause the loss of multiple predicted bounding boxes to be similar, but the difference in the IoU will be very large, which has a great impact on the detection and recognition results.

