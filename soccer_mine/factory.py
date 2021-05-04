from soccer_mine import xpaths

def get_player_profile(response):
    profilemap = {}
    profilemap['name'] = response.xpath(xpaths.xprofile_name).extract_first().strip()
    for val in response.xpath(xpaths.xprofile_values):
        label = val.xpath('text()').extract_first().strip()
        if val.xpath('span/text()').extract_first() is not None:
            if label not in profilemap:
                profilemap[label] = []
            profilemap[label].append(
                val.xpath('span/text()').extract_first())
        elif val.xpath('span/span/text()').extract_first() is not None:
            profilemap[label] = [key.extract().strip()
                                    for key in val.xpath('span/span/text()')]
    for k, v in profilemap.items():
        if len(v) == 1:
            profilemap[k] = ''.join(v)
    return profilemap


def get_player_teams(response):
    teamlist = []
    for z in response.xpath(xpaths.xteamlist):
        team = {}
        team['name'] = z.xpath('h5/a/text()').extract_first().strip()
        team['details'] = {}
        for team_attribute in z.xpath('div/p'):
            label = team_attribute.xpath('text()').extract_first().strip()
            val_check = team_attribute.xpath(
                'span/a/span/text()').extract_first()
            if val_check is None:
                value = team_attribute.xpath(
                    'span/text()').extract_first().strip()
            else:
                value = team_attribute.xpath(
                    'span/a/span/text()').extract_first().strip()
            team['details'][label] = value
        teamlist.append(team)
    return teamlist


def get_player_skills(response):
    skills = {}
    for skill_section in response.xpath(xpaths.xskilllist):
        title = skill_section.xpath('div/h5/text()').extract_first()
        ss = skill_section.xpath(
            'div/div/p')[0].xpath('span/span/text()').extract_first()
        if ss is None:
            skillMap = []
            for skill in skill_section.xpath('div/div/p'):
                skillMap.append(skill.xpath(
                    'text()').extract_first().strip())
        else:
            skillMap = {}
            for skill in skill_section.xpath('div/div/p'):
                skill_title = skill.xpath('text()').extract_first().strip()
                skill_value = skill.xpath(
                    'span/span/text()').extract_first().strip()
                skillMap[skill_title] = skill_value

        skills[title] = skillMap
    return skills


def get_player_rating(response):
    return response.xpath(xpaths.xrating).extract_first()


def get_player_name(response):
    return response.xpath(xpaths.xname).extract_first().strip()