from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), nullable=False)
    role = db.Column(db.String(50), nullable=False)  # admin, sponsor, influencer

    # Relationships
    influencer = db.relationship('Influencer', backref='user', uselist=False, cascade="all, delete-orphan")
    sponsor = db.relationship('Sponsor', backref='user', uselist=False, cascade="all, delete-orphan")
    ad_requests = db.relationship('AdRequest', backref='influencer', lazy=True)
    campaigns = db.relationship('Campaign', backref='sponsor', lazy=True)

class Campaign(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    budget = db.Column(db.Float, nullable=False)
    visibility = db.Column(db.String(10), nullable=False)  # public, private
    goals = db.Column(db.Text, nullable=False)
    niche = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(10), nullable=False)
    flagged = db.Column(db.Boolean, default=False, nullable=False) 
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    # Relationships
    ad_requests = db.relationship('AdRequest', backref='campaign', lazy=True)
    campaign_requests = db.relationship('CampaignRequest', backref='campaign', lazy=True)

class AdRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    campaign_id = db.Column(db.Integer, db.ForeignKey('campaign.id'), nullable=False)
    influencer_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    messages = db.Column(db.Text, nullable=True)
    requirements = db.Column(db.Text, nullable=False)
    payment_amount = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(10), nullable=False)  # Pending, Accepted, Rejected
    complete = db.Column(db.Boolean, default=False, nullable=False)
    complete_confirmed = db.Column(db.Boolean, default=False, nullable=False)
    payment = db.Column(db.Boolean, default=False, nullable=False)

    # Relationships
    influencer = db.relationship('User', backref='ad_requests', foreign_keys=[influencer_id])
    campaign = db.relationship('Campaign', backref='ad_requests', foreign_keys=[campaign_id])

class Influencer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(150), nullable=False)
    profile_picture = db.Column(db.String(150), nullable=True)
    niche = db.Column(db.String(50), nullable=False)
    reach = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    platform = db.Column(db.String(150), nullable=False)  # This will store the social media platforms as a comma-separated string
    flagged = db.Column(db.Boolean, default=False)

class Sponsor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(150), nullable=False)
    company = db.Column(db.String(100), nullable=False)
    industry = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    # Relationships
    user = db.relationship('User', backref='sponsor', uselist=False, cascade="all, delete-orphan")

class CampaignRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    campaign_id = db.Column(db.Integer, db.ForeignKey('campaign.id'), nullable=False)
    influencer_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    messages = db.Column(db.Text, nullable=True)
    status = db.Column(db.String(10), nullable=False)  # Pending, Accepted, Rejected
    complete = db.Column(db.Boolean, default=False, nullable=False)
    complete_confirmed = db.Column(db.Boolean, default=False, nullable=False)
    payment = db.Column(db.Boolean, default=False, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp(), nullable=False)

    # Relationships
    campaign = db.relationship('Campaign', backref='campaign_requests', lazy=True)
    influencer = db.relationship('User', backref='campaign_requests', foreign_keys=[influencer_id])