                             Model Architecture Planning

Membership:
        slug
        type
        price
        stripe plan id

UserMembership:
        user
        stripe_id
        membership_type

Subscription :
        user_membership
        stripe_subscription_id
        active

Course  :
        creator
        slug
        title
        description
        allowed_memberships  foreignkey to (Membership)


Lesson  :
        course    foreignkey to (Course)
        slug
        title
        video
        thumbnail
        position


stripe_product_id = prod_Fp6ElFSsNl5qtf
stripe_plan_id - Free = plan_Fp6HzxADXG8ePX
stripe_plan_id - Professional = plan_Fp6Ic51jDqP7US
stripe_plan_id - Enterprise = plan_Fp6JYETJn9diCD
