# iOS App: Free and Paid Versions

*Research saved: 2026-02-01*

## Two Main Approaches

### 1. Single App with In-App Purchases (Recommended)
- One app listing, free to download
- Lock premium features behind a paywall
- Use StoreKit for purchases (subscriptions or one-time unlock)
- Apple takes 15-30% cut (15% for small business program <$1M/year)
- Easier to maintain, better discoverability

### 2. Two Separate Apps (Legacy Approach)
- "App" (free) and "App Pro" (paid upfront)
- Requires maintaining two codebases or build configurations
- Less common now — users expect freemium model
- Harder to convert free users to paid

## Best Practice Today

**Single app with freemium model:**
- Free tier with core features to hook users
- Premium unlock via subscription or one-time purchase
- Subscriptions preferred by Apple (better ranking, recurring revenue)

## Monetization Options

| Model | Pros | Cons |
|-------|------|------|
| Subscription | Recurring revenue, Apple promotes these | Users hesitant to commit |
| One-time purchase | Simple, users prefer owning | No recurring revenue |
| Consumables | Good for games/credits | Complex to balance |
| Freemium + Ads | Dual revenue stream | Can annoy users |

## Technical Implementation

### StoreKit 2 (Native)
- Modern Swift API for in-app purchases
- Handles transactions, receipts, subscription status
- Server-side validation recommended for security

### RevenueCat (Third-Party)
- Simplifies IAP implementation significantly
- Cross-platform (iOS, Android, web)
- Analytics, A/B testing, paywalls
- Free tier available for small apps

### Frameworks
- **Native:** Swift + SwiftUI (best performance, Apple's preference)
- **Cross-platform:** 
  - React Native (JavaScript, good ecosystem)
  - Flutter (Dart, fast UI development)

## App Store Guidelines

- Must use Apple's IAP for digital goods/features (30% / 15% cut)
- Physical goods can use external payment
- Can't mention external payment options for digital content
- Subscriptions must clearly state terms

## Implementation Checklist

1. [ ] Define free vs premium feature split
2. [ ] Choose monetization model (subscription vs one-time)
3. [ ] Set up App Store Connect products
4. [ ] Implement StoreKit 2 or RevenueCat
5. [ ] Add paywall UI
6. [ ] Handle restore purchases
7. [ ] Server-side receipt validation (recommended)
8. [ ] Test with sandbox accounts

## Resources

- [StoreKit 2 Documentation](https://developer.apple.com/documentation/storekit)
- [RevenueCat Docs](https://docs.revenuecat.com/)
- [App Store Review Guidelines](https://developer.apple.com/app-store/review/guidelines/)
