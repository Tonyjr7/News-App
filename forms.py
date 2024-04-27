from django import forms

class NewsFilterForm(forms.Form):
    
    COUNTRIES = [
    ('ae', 'United Arab Emirates'),
    ('ar', 'Argentina'),
    ('at', 'Austria'),
    ('au', 'Australia'),
    ('be', 'Belgium'),
    ('bg', 'Bulgaria'),
    ('br', 'Brazil'),
    ('ca', 'Canada'),
    ('ch', 'Switzerland'),
    ('cn', 'China'),
    ('co', 'Colombia'),
    ('cr', 'Costa Rica'),
    ('cz', 'Czech Republic'),
    ('de', 'Germany'),
    ('eg', 'Egypt'),
    ('fr', 'France'),
    ('gb', 'United Kingdom'),
    ('gr', 'Greece'),
    ('hr', 'Croatia'),
    ('hk', 'Hong Kong'),
    ('hu', 'Hungary'),
    ('id', 'Indonesia'),
    ('ie', 'Ireland'),
    ('il', 'Israel'),
    ('in', 'India'),
    ('it', 'Italy'),
    ('jp', 'Japan'),
    ('kr', 'South Korea'),
    ('lt', 'Lithuania'),
    ('lv', 'Latvia'),
    ('ma', 'Morocco'),
    ('mx', 'Mexico'),
    ('my', 'Malaysia'),
    ('ng', 'Nigeria'),
    ('nl', 'Netherlands'),
    ('no', 'Norway'),
    ('nz', 'New Zealand'),
    ('ph', 'Philippines'),
    ('pl', 'Poland'),
    ('pt', 'Portugal'),
    ('ro', 'Romania'),
    ('rs', 'Serbia'),
    ('ru', 'Russia'),
    ('sa', 'Saudi Arabia'),
    ('se', 'Sweden'),
    ('sg', 'Singapore'),
    ('sk', 'Slovakia'),
    ('th', 'Thailand'),
    ('tr', 'Turkey'),
    ('tw', 'Taiwan'),
    ('ua', 'Ukraine'),
    ('us', 'United States'),
    ('ve', 'Venezuela'),
    ('za', 'South Africa')
]


    CATEGORIES = [
    ('general', 'General'),
    ('business', 'Business'),
    ('entertainment', 'Entertainment'),
    ('health', 'Health'),
    ('science', 'Science'),
    ('sports', 'Sports'),
    ('technology', 'Technology'),
]

    country = forms.ChoiceField(choices=COUNTRIES, label='Select Country')
    category = forms.ChoiceField(choices=CATEGORIES, label='Select Category')
